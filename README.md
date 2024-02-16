# ClassEval: Manually-Crafted Benchmark on Class-level Code Generation

ClassEval is the first class-level code generation benchmark described in the paper ["ClassEval: A Manually-Crafted Benchmark
for Evaluating LLMs on Class-level Code Generation"](http://arxiv.org/abs/2308.01861). 

## Updates
- 2023-08-05: Initial benchmark release
- 2023-09-04: Add Huggingface support
- 2024-1-3: Release official version v1.0.0

## Benchmark Dataset

We manually build ClassEval of 100 class-level Python coding tasks, consists of 100 classes and 412 methods, and average 33.1 test cases per class.

For 100 class-level tasks, diversity is maintained by encompassing these tasks over a wide spectrum of topics, including *Management Systems*, *Data Formatting*, *Mathematical Operations*, *Game Development*, *File Handing*, *Database Operations* and *Natural Language Processing*.

For 412 methods, they have been constructed with diverse dependencies, including (i) *Library Dependency*, where the methods rely on specific external libraries; (ii) *Field Dependency*, in which the methods are contingent on class instance variables, or fields; (iii) *Method Dependency*, where the methods are dependent on other methods within the same class; and (iv) *Standalone*, wherein the methods operate independently without reliance on fields, other methods, or external libraries. 

## Benchmark Format

ClassEval has been meticulously structured and saved in the JSON format, accessible at [ClassEval Data](https://github.com/FudanSELab/ClassEval/blob/master/data/ClassEval_data.json). The specific data fields for each task are delineated as follows:

* task_id: the unique identifier for each task.

* skeleton: the class skeleton, including all input descriptions in our class-level coding tasks. 

* test: all test cases for the whole class.

* solution_code: the ground-truth class-level code for each task.

More fine-grained class-level information from the class skeleton, including:

* import_statement: the import statements for each task.

* class_name: the name of the class.

* class_description: a concise description of the purpose and functionality of the class.

* class_constructor: the whole constructor of the class.

* fields: the fields defined in the class_constructor.

Detailed information for each method in the "methods_info" field, including:

* method_name: the method signature.

* method_input: the method contract design, including all input descriptions in the method.

* test_code: the test cases for the method.

* solution_code: the ground-truth method-level code.

* dependencies: the dependency information of the method.

For more details in benchmark construction, go [here](./data/README.md).

The comparison of the inputs for the ClassEval, HumanEval, and MBPP benchmarks is illustrated in the following figures:

<img src="output\images\classeval example.png" alt="other benchmark example" style="zoom: 5%;" />

<img src="output\images\other benchmark example.png" alt="other benchmark example" style="zoom: 8%;" />

The comparison of test case examples from the ClassEval, HumanEval, and MBPP datasets is depicted in the following figure:

<img src="output\images\test example.png" alt="test example" style="zoom: 28%;" />


## Generation Strategies

We devise three distinct generation strategies for evaluating LLMs on class-level code generation:

**Holistic Generation**: the model is asked to generate the entire class all at once with the class skeleton as inputs. 

**Incremental Generation**: the model is asked to generate the class in a method-by-method manner. Each iteration is based on the method bodies that have been generated in previous iterations. The iterative process repeats until all methods in the class are generated.  

**Compositional Generation**: the model is asked to generate the class in a method-by-method manner. Each iteration is independent, without considering the other generated methods. All the generated methods are assembled to form the class lastly.

The holistic generation strategy evaluates the model ability of handling long and complicated coding tasks all at once, while the incremental and compositional generation strategies focus on step-by-step class completion. The incremental strategy simulates progressive software development, where developers incrementally implement current methods based on existing ones. In constrast, the compositional strategy simulates real-world programming scenarios, where developers implement current methods based on other available method signatures.

## Implementation

We consider two sampling methods for code generation: (i) nucleus sampling, where five solution code samples are randomly generated for each task with a temperature of 0.2 and default top_p, and (ii) greedy sampling, where only one single solution code sample is generated for each task using greedy decoding, i.e., setting the “do_sample” hyperparameter to false (temperature of 0). Our experiments are run on a computational infrastructure comprising eight A800-80G GPUs.

## Results

### Overall Correctness

The following figure shows the class-level and method-level Pass@1 with greedy sampling of studied LLMs on ClassEval and HumanEval:

<img src="output\images\C_pass1_bar.png" alt="C_pass1_bar" style="zoom: 29%;" />

The following table presents the class-level and method-level Pass@k
with nucleus sampling on ClassEval:

<img src="output\images\pass@k.png" alt="pass@k" style="zoom: 50%;" />

Notably, we only present the best class-level Pass@1 (and corresponding method-level Pass@1) for each model among the three generation strategies.

### Generation Strategies

The following figures compare the class-level Pass@5 and method-level Pass@5
of three different generation strategies (i.e., holistic, incremental,
and compositional generation)

<img src="output\images\C_pass5.png" alt="pass@k" style="zoom: 45%;" />

<img src="output\images\M_pass5.png" alt="pass@k" style="zoom: 45%;" />

## Usage

Ensure you're using the right setup and following the proper directory structure to seamlessly evaluate class-level code generation with our tool.

### 🛠️ Setup

1. Environment Setup

Ensure you're running Python 3.8 or newer. We recommend setting up a virtual environment:
```
$ conda create -n classeval python=3.8
$ conda activate classeval
```

2. Repository Setup

Clone the repository and install necessary dependencies:
```
$ git clone https://github.com/FudanSELab/ClassEval
$ pip install -e ClassEval
```

### 📁 Data & Output Structure
**Data**: Ensure `ClassEval_data.json` is placed in the `data` directory

**Model Outputs**: Keep all model-generated outputs in `output/model_output`. These outputs should be in JSON format, with predictions under the `predict` key, pointing to the list of generated code samples.

### 🔍 Deep Dives
**Class-Level Code Generation**: Dive into our implementation details [here](https://github.com/FudanSELab/ClassEval/blob/master/generation).

**Evaluation Process**: Explore in-depth [here](https://github.com/FudanSELab/ClassEval/blob/master/classeval_evaluation).

## Hugging Face Support

To access ClassEval on Hugging Face, follow this link: <https://huggingface.co/datasets/FudanSELab/ClassEval>

To load the dataset, use the code below:
```python
from datasets import load_dataset
dataset = load_dataset("FudanSELab/ClassEval")
```

## License

This repository is under [MIT](https://github.com/FudanSELab/ClassEval/blob/master/LICENSE) license. But the data is distributes through [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.

## Contributors

Xueying Du xueyingdu21@m.fudan.edu.cn

[Mingwei Liu](https://mingwei-liu.github.io/) liumingwei@fudan.edu.cn

Kaixin Wang kxwang23@m.fudan.edu.cn

Hanlin Wang wanghanlin23@m.fudan.edu.cn

Junwei Liu jwliu22@m.fudan.edu.cn

Yixuan Chen 23212010005@m.fudan.edu.cn

Jiayi Feng 23210240148@m.fudan.edu.cn

Chaofeng Sha cfsha@fudan.edu.cn

Xin Peng pengxin@fudan.edu.cn

Yiling Lou yilinglou@fudan.edu.cn

## Citation

```
@misc{du2023classeval,
      title={ClassEval: A Manually-Crafted Benchmark for Evaluating LLMs on Class-level Code Generation}, 
      author={Xueying Du and Mingwei Liu and Kaixin Wang and Hanlin Wang and Junwei Liu and Yixuan Chen and Jiayi Feng and Chaofeng Sha and Xin Peng and Yiling Lou},
      year={2023},
      eprint={2308.01861},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```


