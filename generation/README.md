## Generation 
We provide `inference.py` script to to produce class-level code outputs, supporting various models and generation strategies.

Navigate to the generation directory and execute the following command:
```
python inference.py \
--model 0 \
--checkpoint model_path \
--output_path model_output.json \
--greedy 1 \
--data_path ../data/ClassEval_data.json \
--cuda 0 1 \
--generation_strategy 0

```

## Parameter Guide

### Supported Models

Specify the model using the `--model` argument. Each model might have its own unique API.

Supported models:

0: Instruct_CodeGen
1: WizardCoder
2: Instruct_StarCoder
...

For a detailed list of models and their respective identifiers, check the help associated with the `--model` parameter in `inference.py`. To integrate new models, append the appropriate model identifier in `inference.py` and ensure its API is also added.

Currently, we cater to 9 models: Instruct_CodeGen, WizardCoder, Instruct_StarCoder, InCoder, PolyCoder, SantaCoder, Vicuna, ChatGLM, GPT-3.5, and GPT-4. For GPT-3.5 and GPT-4, supply your personal OpenAI key using the `--openai_key` parameter.

### Sampling Methods

Specify your desired sampling method with the `--greedy` argument:

- 0: Nucleus sampling. 
- 1: Greedy sampling.

For nucleus sampling, ensure you also provide the sample number using the `--sample` argument.

### Generation Strategies
Determine your generation strategy with the `--generation_strategy` argument:

- 0: Holistic Generation
- 1: Incremental Generation
- 2: Compositional Generation

For insights on the practical implementation of these generation strategies, see the `def pipeline` within `inference_pipeline.py`.

### Further Parameters

For a comprehensive overview of all parameters and their valid values, either peruse the `inference.py` script or run with the `--help` flag.

### Prompt Desgin


We can categorize all studied LLMs into three distinct classes based on their capabilities: LLMs with Instruction-Following (IF) ability via instruction tuning, LLMs without instruction tuning but possessing the ability of "filling-in-the-middle" (FIM), and LLMs lacking both IF and FIM abilities.

#### LLMs with IF Ability

Following the common practice of prompting LLMs with IF ability like WizardCoder, we set their prompts
of two parts: (i) a system prompt as the beginning sentence to initialize the model, and followed by (ii) a task instruction to describe the goal of the task.

**System Prompt**: *Provided below is an instruction detailing a task. Compose a response that aptly fulfills the request.*

**Instruction-H**: *Please complete the class **${Class Name}** in the subsequent code. **${Class Skeleton}***

Refer to Figure 2 in the paper for details on the class skeleton.

**Instruction-I**: *Please complete the method **${Method Name}** within the following class **${Class Name}. ${Class-level Info} ${Generated Methods with Contract Designs} ${Target Method Contract Design}***

We provide a more explicit representation of the incremental generation process in the following figure: 

<img src="incremental generation.png" alt="Incremental Generation Process" style="zoom: 5%;" />

**Instruction-C**: *Please complete the method ${Method Name} within the following class **${Class Name}**. **${Class-level Info} ${Other Method Signatures} ${Target Method Contract Design}***

**${Class-level Info}** encompasses import statements, class name, class description, and class constructor, while **${Target Method Contract Design}** includes method signature, functional description, parameter/return description, and example input/output. Detailed content for each component can be found in Figure 2 of the paper.

#### LLMs with FIM Ability

The prompt of these models is the code context without any instruction: (i) for holistic generation, the
prompt is just the class skeleton; (ii) for incremental generation, the prompt in each iteration includes the class-level information, generated methods, and the target method contract design; (iii) for
compositional generation, the prompt for each method includes the class-level information, other method signatures, and the target method contract design. 

To stimulate FIM ability, we've included a placeholder <insert> where method bodies need to be generated. Here's an example for holistic generation:

```python
${Class-level Info}
${Method_1 Contract Design}
<insert>
${Method_2 Contract Design}
<insert>
...
${Method_N Contract Design}
<insert>
```

#### with Neither IF nor FIM Ability
These models utilize input similar to LLMs with FIM ability but without any <insert> placeholders.

