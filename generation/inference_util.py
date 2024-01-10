import re
from enum import Enum

class InferenceUtil:

    @staticmethod
    def generate_prompt(instruction, type = 1):
        if type == 1:
            return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:"""

        if type == 2:
            return f"""You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Instruction:
{instruction}

@@ Response:
"""

    @staticmethod
    def get_leading_spaces(string):
        return len(string) - len(string.lstrip())

    @staticmethod
    def del_segment_notation(code):
        pattern = r'(""".*?""")'
        result = re.sub(pattern, '', code, flags = re.DOTALL)
        return result

    @staticmethod
    def get_method_signature(code, method_name):
        method_def_prefix = "def " + method_name + '('
        code_segment = code.split('):')
        for segment in code_segment:
            if method_def_prefix in segment:
                return "    " + segment + "):"
        return ""

    @staticmethod
    def add_desc_to_init(desc, class_init):
        class_init_list = class_init.split('\n')
        class_init_list[0] += " \n" + desc
        class_init = '\n'.join(class_init_list)
        return class_init

    @staticmethod
    def extract_method_code(code, method_name):
        # extract code of method {method_name} from {code}
        if "### Response:" in code:
            code_list = code.split("### Response:")[1].split('\n')
        elif "@@ Response" in code:
            code_list = code.split("@@ Response")[1].split('\n')
        else:
            code_list = code.split('\n')
        method_code_list = []
        is_this_method = False
        leading_space = 0
        first_cont_line_space = -1
        line_notation_mark = 0
        # extract generated method code corresponding method_name, the strategy is to find the line
        # has "def methodname(...)" and following lines have more leading spaces than the first "def" line
        for line in code_list:
            if line == "        \"\"\"" or line == "    \"\"\"":
                line_notation_mark = line_notation_mark + 1
            method_def_prefix = "def " + method_name + '('
            if method_def_prefix in line:
                is_this_method = True
                leading_space = InferenceUtil.get_leading_spaces(line)
                method_code_list.append(' ' * (4 - leading_space) + line)
            elif is_this_method:
                if InferenceUtil.get_leading_spaces(line) > leading_space or len(line) == 0 or line == "```" or line == '\r':
                    if line == "```" or line == '\r':
                        continue
                    if first_cont_line_space == -1 and len(line) != 0:
                        first_cont_line_space = InferenceUtil.get_leading_spaces(
                            line)
                    if first_cont_line_space - leading_space > 4:
                        method_code_list.append(line)
                    else:
                        method_code_list.append(
                            ' ' * (4 - leading_space) + line)
                else:
                    break

        if line_notation_mark % 2 == 1:
            method_code_list.append("        \"\"\"")

        method_code = '\n'.join(method_code_list)
        return method_code
    

class ModelName(Enum):
    Instruct_CodeGen = 0
    WizardCoder = 1
    Instruct_StarCoder = 2
    InCoder = 3
    PolyCoder = 4
    SantaCoder = 5
    Vicuna = 6
    ChatGLM = 7
    GPT_3_5 = 8
    GPT_4 = 9
    others = 10
    Magicoder = 11
    CodeGeeX2 = 12
    DeepSeekCoder_inst = 13

class GenerationStrategy(Enum):
    Holistic = 0
    Incremental = 1
    Compositional = 2