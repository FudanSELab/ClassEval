# ClassEval: Manually-Crafted Benchmark on Class-level Code Generation

ClassEval is the first class-level code generation benchmark described in the paper ["ClassEval: A Manually-Crafted Benchmark
for Evaluating LLMs on Class-level Code Generation"](http://arxiv.org/abs/2308.01861). 

## Updates
- 2023-08-05: Initial Benchmark Release

### Plan
- Huggingface Support
- ...

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

 we consider two sampling methods for code generation: (i) nucleus sampling, where five solution code samples are randomly generated for each task with a temperature of 0.2 and default top_p, and (ii) greedy sampling, where only one single solution code sample is generated for each task using greedy decoding, i.e., setting the “do_sample” hyperparameter to false (temperature of 0). Our experiments are run on a computational infrastructure comprising eight A800-80G GPUs

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

### Installation

Create a virtual environment, python version >= 3.8.

```
$ conda create -n classeval python=3.8
$ conda activate classeval
```
Check out and install this repository:
    
```
$ git clone https://github.com/FudanSELab/ClassEval
$ pip install -e ClassEval
```

### Prerequisites:

-  Place `ClassEval_data.json` in the `data` directory for seamless access.

- Store all model-generated outputs in the `output/model_output` directory. Ensure these are in JSON format, under the key `predict` which maps to the list of generated code samples.

### Evaluation

To evaluate the models' performance on class-level code generation task, we provide `evaluation.py`. Navigate to the `classeval_evaluation` directory and run:

```
python evaluation.py --source_file_name model_output --eval_data ClassEval_data --greedy 1
```

- `--source_file_name`: Specifies the filenames pertaining to model outputs.
- `--greedy`: Specifies the sampling methods for generation. Permissible values:
    - 0: Nucleus sampling.
    - 1: Greedy sampling.
- `--eval_data`:  Refers to the benchmark data file, named `ClassEval_data` in the current rendition.

Our nucleus sampling encompasses 5 samples. During the evaluation, we restrict our scope to the results of pass@1, pass@3, and pass@5. If there's a need to generate a different sample size, it necessitates adjustments `cal_metrics_pass_at_k(model_list, k, n)` in the `evaluation.py` code, where k represents the 'k' in pass@k and n stands for the sample count.

### Output

The evaluation results are systematically cataloged in the `output/result` directory:

- **pass_at_k_result.json**: This file aggregates the pass@k metrics across all models' outputs.

- **detailed_result.json**: Dive deep with a meticulous examination of every test case across models' outputs.

The runtime logs for every test case are in the  `log` directory.

## License

This repository is under [MIT](https://github.com/FudanSELab/ClassEval/blob/master/LICENSE) license. But the data is distributes through [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.

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


