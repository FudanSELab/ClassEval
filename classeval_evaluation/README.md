
## Evaluation

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

## Output

The evaluation results are systematically cataloged in the `output/result` directory:

- **pass_at_k_result.json**: This file aggregates the pass@k metrics across all models' outputs.

- **detailed_result.json**: Dive deep with a meticulous examination of every test case across models' outputs.

The runtime logs for every test case are in the  `log` directory.
