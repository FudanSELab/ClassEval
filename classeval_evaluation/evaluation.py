import argparse
import json
import os
from test_pipeline import AutoTest
from path_util import PathUtil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source_file_name",
        type=str,
        default="model_output",
        help="source of model output",
    )
    parser.add_argument(
        "--greedy",
        type=int,
        default=1,
        help="whether the model result is greedy or not",
    )
    parser.add_argument(
        "--eval_data",
        type=str,
        default='ClassEval_data',
        help="ClassEval data",
    )
    args = parser.parse_args()

    AutoT = AutoTest(args.eval_data)
    model_list = [args.source_file_name]

    for model_name in model_list:
        file_path = PathUtil().model_output_data(model_name, "json")
        AutoT.test_pipeline(model_name, file_path)

    AutoT.evaluate(model_list)
    result = {}
    if args.greedy == 1:
        result["pass_1_greedy"] = AutoT.cal_metrics_pass_at_k(model_list, 1, 1)
    else:
        result["pass_1"] = AutoT.cal_metrics_pass_at_k(model_list, 1, 5)
        result["pass_3"] = AutoT.cal_metrics_pass_at_k(model_list, 3, 5)
        result["pass_5"] = AutoT.cal_metrics_pass_at_k(model_list, 5, 5)
    save_path = PathUtil().test_result_data("pass_at_k_result", 'json')

    if os.path.exists(save_path):
        with open(save_path, encoding='utf-8') as file:
            ori_data = json.load(file)

        if args.greedy == 1:
            if "pass_1_greedy" in ori_data:
                ori_data["pass_1_greedy"][args.source_file_name] = result["pass_1_greedy"][args.source_file_name]
            else:
                ori_data["pass_1_greedy"] = result["pass_1_greedy"]
        else:
            if "pass_1" in ori_data:
                ori_data["pass_1"][args.source_file_name] = result["pass_1"][args.source_file_name]
                ori_data["pass_3"][args.source_file_name] = result["pass_3"][args.source_file_name]
                ori_data["pass_5"][args.source_file_name] = result["pass_5"][args.source_file_name]
            else:
                ori_data["pass_1"] = result["pass_1"]
                ori_data["pass_3"] = result["pass_3"]
                ori_data["pass_5"] = result["pass_5"]
    else:
        ori_data = result

    with open(save_path, 'w') as f:
        json.dump(ori_data, f, indent=4, sort_keys=True)