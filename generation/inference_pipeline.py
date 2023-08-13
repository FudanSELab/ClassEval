import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, AutoModel
import json
from tqdm import tqdm
from inference_util import InferenceUtil, ModelName, GenerationStrategy
import openai

class InferencePipeline:

    def __init__(self, args):
        with open(args.data_path, 'r', encoding = 'utf-8') as f:
            self.file_cont = json.load(f)
        self.greedy = args.greedy
        self.output_path = args.output_path
        self.cuda = args.cuda
        self.generation_strategy = args.generation_strategy
        self.model_name = args.model
        self.checkpoint = args.checkpoint
        self.temperature = args.temperature
        self.max_length = args.max_length
        self.openai_key = args.openai_key
        self.openai_base = args.openai_base

        self.get_model_tokenizer_and_config()
        self.SAMPLE_NUMS = 1 if self.greedy == 1 else args.sample
        self.do_sample = False if self.greedy == 1 else True

    def get_model_tokenizer_and_config(self):
        if self.model_name == ModelName.GPT_3_5.value or self.model_name == ModelName.GPT_4.value:
            return
        elif self.model_name == ModelName.ChatGLM.value:
            self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint, trust_remote_code = True)
            self.model = AutoModel.from_pretrained(self.checkpoint, trust_remote_code = True).half().to(self.cuda)
            self.model = self.model.eval()
        elif self.model_name == ModelName.PolyCoder.value or self.model_name == ModelName.SantaCoder.value:
            self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint, trust_remote_code = True)
            self.model = AutoModelForCausalLM.from_pretrained(self.checkpoint, trust_remote_code = True).to(self.cuda)
            self.model = self.model.eval()
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.generation_config = GenerationConfig(
                temperature = 0 if self.greedy == 1 else self.temperature,
                eos_token_id = self.tokenizer.eos_token_id,
                pad_token_id = self.tokenizer.pad_token_id
            )
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint, trust_remote_code = True)
            self.model = AutoModelForCausalLM.from_pretrained(self.checkpoint, trust_remote_code = True, torch_dtype = torch.float16).to(self.cuda)
            self.model = self.model.eval()
            self.generation_config = GenerationConfig(
                temperature = 0 if self.greedy == 1 else self.temperature,
                eos_token_id = self.tokenizer.eos_token_id,
                pad_token_id = self.tokenizer.pad_token_id
            )

    def save_result(self, result):
        with open(self.output_path, 'w', encoding = 'utf-8') as f:
            json.dump(result, f, indent=4)

    def model_generate(self, prompt):
        if self.model_name == ModelName.GPT_3_5.value or self.model_name == ModelName.GPT_4.value:
            openai.api_key = self.openai_key
            openai.api_base = self.openai_base
            if self.model_name == ModelName.GPT_3_5.value:
                response = openai.ChatCompletion.create(
                    max_tokens=self.max_length,
                    temperature=0 if self.greedy == 1 else self.temperature,
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
            elif self.model_name == ModelName.GPT_4.value:
                response = openai.ChatCompletion.create(
                    max_tokens=self.max_length,
                    temperature=0 if self.greedy == 1 else self.temperature,
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
            outputs = response.choices[0]["message"]["content"]
        elif self.model_name == ModelName.ChatGLM.value:
            outputs, _ = self.model.chat(self.tokenizer, prompt, temperature = self.temperature, do_sample = self.do_sample)
        else:
            input_ids = self.tokenizer.encode(prompt, return_tensors = "pt", max_length = self.max_length, truncation = True).to(self.cuda)
            outputs = self.model.generate(input_ids, generation_config = self.generation_config, 
                                            max_length = self.max_length, do_sample = self.do_sample)
            outputs = self.tokenizer.decode(outputs[0], skip_special_tokens = True)
        return outputs

    def construct_prompt(self, strategy, info):
        prompt = ""
        if strategy == GenerationStrategy.Holistic:
            if self.model_name == ModelName.PolyCoder.value or self.model_name == ModelName.SantaCoder.value:
                skeleton = info['skeleton']
                prompt = skeleton
            else:
                class_name = info['class_name']
                skeleton = info['skeleton']
                instruction = f"Please complete the class {class_name} in the following code."
                instruction = instruction + '\n' + skeleton
                prompt = InferenceUtil.generate_prompt(instruction)

        elif strategy == GenerationStrategy.Incremental:
            if self.model_name == ModelName.PolyCoder.value or self.model_name == ModelName.SantaCoder.value:
                prompt = info['skeleton']
            else:
                prompt = InferenceUtil.generate_prompt(info['instruction'] + info['skeleton'])

        elif strategy == GenerationStrategy.Compositional:
            if self.model_name == ModelName.PolyCoder.value or self.model_name == ModelName.SantaCoder.value:
                prompt = info['skeleton']
            else:
                prompt = InferenceUtil.generate_prompt(info['instruction'] + info['skeleton'])

        return prompt

    def post_process(self, result):
        if self.generation_strategy == GenerationStrategy.Incremental.value:
            for cont in result:
                pred = []
                for result in cont['predict']:
                    pred.append(result[-1])
                cont['predict'] = pred
        elif self.generation_strategy == GenerationStrategy.Compositional.value:
            for cont in result:
                cont['raw_output'] = cont['predict'].copy()
            for cont in result:
                cont['predict'] = []
                for raw_output in cont['raw_output']:
                    class_code = '\n'.join(cont['import_statement']) + '\n' + cont['class_constructor']
                    for i in range(len(raw_output)):
                        method_name = cont['methods_info'][i]['method_name']
                        code = raw_output[i]
                        method_code = InferenceUtil.extract_method_code(code, method_name)
                        class_code += '\n\n' + method_code
                    cont['predict'].append(class_code)

    def pipeline(self):
        if self.generation_strategy == GenerationStrategy.Holistic.value:
            result = []
            for cont in tqdm(self.file_cont):
                pred = []
                try:
                    prompt = self.construct_prompt(GenerationStrategy.Holistic, cont)
                    for _ in range(self.SAMPLE_NUMS):
                        outputs = self.model_generate(prompt)
                        pred.append(outputs)
                    cont['predict'] = pred
                    result.append(cont)
                    self.save_result(result)

                except Exception as e:
                    print(e)
                    print("IDX: ", cont['task_id'])

        elif self.generation_strategy == GenerationStrategy.Incremental.value:
            result = []
            for cont in tqdm(self.file_cont):
                cont['predict'] = []
                cont['raw_output'] = []
                for _ in range(self.SAMPLE_NUMS):
                    pred = []
                    raw_output = []
                    try:
                        class_name = cont['class_name']
                        methods_info = cont['methods_info']
                        imports = '\n'.join(cont['import_statement'])
                        class_init = InferenceUtil.add_desc_to_init(cont['class_description'], cont['class_constructor'])
                        class_text = imports + '\n' + class_init
                        for method in methods_info:
                            # construct prompt
                            method_name = method['method_name']
                            inst = f"please complete {method_name} method in the following class {class_name}\n\n"
                            class_text_desc = class_text + "\n\n    " + method['method_description']
                            prompt = self.construct_prompt(GenerationStrategy.Incremental, {"instruction":inst, "skeleton": class_text_desc})

                            # generate model output
                            outputs = self.model_generate(prompt)
                            raw_output.append(outputs)

                            # extract valid generated code
                            generated_method_code = InferenceUtil.extract_method_code(outputs, method_name)
                            class_text += '\n\n' + generated_method_code
                            pred.append(class_text)

                        cont['predict'].append(pred)
                        cont['raw_output'].append(raw_output)
                        
                    except Exception as e:
                        print(e)
                        print("IDX: ", cont['task_id'])
                result.append(cont)
                self.save_result(result)

        elif self.generation_strategy == GenerationStrategy.Compositional.value:
            result = []
            for cont in tqdm(self.file_cont):
                cont['predict'] = []
                for _ in range(self.SAMPLE_NUMS):
                    pred = []
                    try:
                        class_name = cont['class_name']
                        methods_info = cont['methods_info']
                        imports = '\n'.join(cont['import_statement'])
                        class_init = InferenceUtil.add_desc_to_init(cont['class_description'], cont['class_constructor'])
                        for method_to_generate in methods_info:
                            class_text = imports + '\n' + class_init
                            # gather each method's signature to consruct class level skeleton
                            for method in methods_info:
                                if method['method_name'] == method_to_generate['method_name']:
                                    continue
                                class_text += InferenceUtil.get_method_signature(method['method_description'], method['method_name']) + "\n        pass\n\n"
                            # construct prompt
                            method_name = method_to_generate['method_name']
                            inst = f"please complete {method_name} method in the following class {class_name}\n\n"
                            class_text_desc = class_text + "\n\n    " + method_to_generate['method_description']
                            prompt = self.construct_prompt(GenerationStrategy.Compositional, {"instruction":inst, "skeleton": class_text_desc})

                            # generate model output
                            outputs = self.model_generate(prompt)
                            pred.append(outputs)

                        cont['predict'].append(pred)
                        
                    except Exception as e:
                        print(e)
                        print("IDX: ", cont['task_id'])

                result.append(cont)
                self.save_result(result)
        else:
            print("Unknown Generation Strategy")
            return
        
        self.post_process(result)
        self.save_result(result)