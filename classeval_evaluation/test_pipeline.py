import shutil
import time
from func_timeout import func_set_timeout
import importlib
import unittest
import json
import re
import os
from scipy.special import comb
from path_util import PathUtil

class AutoTest:

    def __init__(self, eval_data_name):
        self.eval_data = self.get_eval_data(eval_data_name)

    def get_eval_data(self, eval_data_name):
        eval_data = {}
        eval_data_path = PathUtil.eval_data(eval_data_name)
        with open(eval_data_path, encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            eval_data[item['task_id']] = item
        return eval_data

    def gen_py_file(self, test_code_name, code_list, test_code):
        cnt = 0
        for code_snippet in code_list:
            test_code_py = code_snippet + '\n' + test_code
            with open(test_code_name + '_' + str(cnt) + '.py', 'w', encoding='utf-8') as f:
                f.write(test_code_py)
            cnt += 1

    def get_leading_spaces(self, string):
        return len(string) - len(string.lstrip())

    def extract_imports(self, code_snippet):
        pattern = r'^import\s.*$|from\s.*\simport.*$'
        imports = re.findall(pattern, code_snippet, re.MULTILINE)
        return imports

    def extract_code(self, text, model_name):
        text = text.rstrip()
        output_split_identifier_list = ["### Response:", "@@ Response:", "[/INST]"]
        for identifier in output_split_identifier_list:
            if identifier in text:
                text = text.split(identifier)[1]
                break

        if "incoder" in model_name:
            # remove <|/ file |>
            if "<|/ file |>" in text:
                text = text.split("<|/ file |>")[0]
            return text

        else:
            pattern_list = [r"```python(.*?)```", r"```ruby(.*?)```", r"```scss(.*?)```",
                            r"```python(.*?)", r"```(.*?)```", r"\[PYTHON\](.*?)\[/PYTHON\]"]
            for pattern in pattern_list:
                try:
                    code = re.findall(pattern, text, re.S)[0]
                    return code
                except:
                    continue

            code_list = text.split("\n")
            removed_lines = []
            for code_line in code_list:
                if code_line.strip().startswith('class'):
                    break
                elif not code_line.strip().startswith('import') and not code_line.strip().startswith('from'):
                    removed_lines.append(code_line)
            code_list = [line for line in code_list if line not in removed_lines]
            text = '\n'.join(code_list)

            wrong_indent_flag = False
            for code_line in text.split("\n"):
                if code_line.strip().startswith('class'):
                    class_signature_line_leading_spaces = self.get_leading_spaces(code_line)
                    if class_signature_line_leading_spaces != 0:
                        wrong_indent_flag = True
                    break
            if wrong_indent_flag:
                final_code_line_list = []
                for code_line in text.split("\n"):
                    cur_leading_spaces = self.get_leading_spaces(code_line)
                    # Keep the relative indentation unchanged
                    final_code_line_list.append(' ' * (cur_leading_spaces - class_signature_line_leading_spaces) + code_line.lstrip())
                text = '\n'.join(final_code_line_list)
            return text

    def add_static_statement(self, code):
        filtered_code_list = []
        for line in code.split('\n'):
            if '@staticmethod' in line:
                continue
            filtered_code_list.append(line)
        code = '\n'.join(filtered_code_list)
        final_code_list = []
        for line in code.split('\n'):
            if line.strip().startswith('def ') and 'self' not in line and 'cls' not in line and self.get_leading_spaces(line) == 4:
                final_code_list.append('    @staticmethod')
            final_code_list.append(line)
        return '\n'.join(final_code_list)

    def gen_code_list(self, file_path):
        code_list = {}

        with open(file_path, 'r', encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            code_list[item['task_id']] = []
            for predict in item['predict']:
                predict = self.extract_code(predict, file_path)
                predict = self.add_static_statement(predict)
                predict = '\n'.join(self.eval_data[item['task_id']]['import_statement']) + '\n' + predict
                code_list[item['task_id']].append(predict)
        return code_list

    @func_set_timeout(5)
    def run_unit_test(self, test_code, test_class, model_name):
        module = importlib.import_module(test_code)
        log_path = PathUtil().log_output_data(model_name + "_log_data", 'log')
        with open(log_path, 'a', encoding='utf-8') as f:
            test_suite = unittest.TestLoader().loadTestsFromTestCase(getattr(module, test_class))
            test_result = unittest.TextTestRunner(stream = f).run(test_suite)

        return test_result

    def test(self, code_num, test_code_name, test_classes, model_name):

        result = {}

        for i in range(code_num):

            test_code = test_code_name + '_' + str(i)
            result[test_code] = {}

            for test_class in test_classes:
                res_item = {}
                try:
                    res = self.run_unit_test(test_code, test_class, model_name)
                    res_item['errors'] = len(res.errors)
                    res_item['failures'] = len(res.failures)
                    res_item['testsRun'] = res.testsRun
                    result[test_code][test_class] = res_item
                except:
                    res_item['errors'] = 0
                    res_item['failures'] = 0
                    res_item['testsRun'] = 0
                    result[test_code][test_class] = res_item

        return result

    def save_result(self, model_name, result, type):
        save_path = PathUtil().test_result_data(
            model_name + "_" + type + '_result', 'json')
        with open(save_path, 'w') as f:
            json.dump(result, f, indent=4, sort_keys=True)

    def test_pipeline(self, model_name, gen_file_path):

        result_dict = {}
        # get generate code list
        code_list = self.gen_code_list(gen_file_path)

        # get test code and generate py file
        for task_id in code_list:
            test_code = self.eval_data[task_id]['test']
            task_code_list = code_list[task_id]
            self.gen_py_file(task_id, task_code_list, test_code)

        # run unit test
        for task_id in code_list:
            task_code_list = code_list[task_id]
            try:
                result = self.test(len(task_code_list), task_id,
                                   self.eval_data[task_id]['test_classes'], model_name)
                result_dict[task_id] = result
            except:
                continue

        # save result
        self.save_result(model_name, result_dict, "class")
        time.sleep(5)
        self.tear_down()

    def get_test_answer(self, test_result):
        if test_result['testsRun'] == 0 or test_result['errors'] == test_result['testsRun']:
            return 'error'
        if test_result['errors'] + test_result['failures'] == 0:
            return 'success'
        if test_result['errors'] + test_result['failures'] < test_result['testsRun']:
            return 'partial_success'
        return 'fail'

    def evaluate(self, model_list):

        result_dict = {}
        for model_name in model_list:
            model_result_path = PathUtil().test_result_data(
                model_name + '_class_result', 'json')
            with open(model_result_path, 'r') as f:
                model_result = json.load(f)
            result_dict[model_name] = {}
            for task in model_result:
                result_dict[model_name][task] = {}
                for test_num in model_result[task]:
                    temp_result = {"success": 0,
                                   "partial_success": 0, "fail": 0, "error": 0}
                    for test_class in model_result[task][test_num]:
                        if test_class not in result_dict[model_name][task]:
                            result_dict[model_name][task][test_class] = {}
                            result_dict[model_name][task]["TestClass"] = {}
                            result_dict[model_name][task]["TestClass"]["ClassEachTestResult"] = [
                            ]
                            result_dict[model_name][task][test_class]['success'] = 0
                            result_dict[model_name][task][test_class]['partial_success'] = 0
                            result_dict[model_name][task][test_class]['fail'] = 0
                            result_dict[model_name][task][test_class]['error'] = 0
                            result_dict[model_name][task][test_class]["EachTestResult"] = [
                            ]
                            result_dict[model_name][task]["TestClass"]["class_success"] = 0
                            result_dict[model_name][task]["TestClass"]["class_partial_success"] = 0
                            result_dict[model_name][task]["TestClass"]["class_fail"] = 0
                        test_answer = self.get_test_answer(
                            model_result[task][test_num][test_class])
                        result_dict[model_name][task][test_class][test_answer] += 1
                        result_dict[model_name][task][test_class]["EachTestResult"].append(
                            test_answer)
                        temp_result[test_answer] += 1
                    if temp_result['success'] == len(model_result[task][test_num]):
                        result_dict[model_name][task]["TestClass"]["class_success"] += 1
                        result_dict[model_name][task]["TestClass"]["ClassEachTestResult"].append(
                            "class_success")
                    elif temp_result['fail'] == 0 and temp_result['error'] == 0:
                        result_dict[model_name][task]["TestClass"]["class_partial_success"] += 1
                        result_dict[model_name][task]["TestClass"]["ClassEachTestResult"].append(
                            "class_partial_success")
                    else:
                        result_dict[model_name][task]["TestClass"]["class_fail"] += 1
                        result_dict[model_name][task]["TestClass"]["ClassEachTestResult"].append(
                            "class_fail")

        save_path = PathUtil().test_result_data("detailed_result", 'json')
        with open(save_path, 'w') as f:
            json.dump(result_dict, f, indent=4, sort_keys=True)

    def cal_pass_at_k(self, n, k, k_success):
        total_combinations = comb(k, n)
        if k - k_success >= n:
            without_k_success_combinations = comb(k - k_success, n)
        else:
            without_k_success_combinations = 0

        with_k_success_combinations = total_combinations - without_k_success_combinations

        pass_at_k = with_k_success_combinations / total_combinations

        return pass_at_k

    def cal_metrics_pass_at_k(self, model_list, n, k):

        file_path = PathUtil().test_result_data("detailed_result", 'json')
        with open(file_path, 'r') as f:
            test_result = json.load(f)

        result = {}

        for model_name in model_list:
            sum_num = 0
            success_num = 0
            class_success_num = 0
            class_num = 0
            partial_success_num = 0
            partial_success_class_num = 0
            for task in test_result[model_name]:
                class_num += 1
                for test_class in test_result[model_name][task]:
                    try:
                        if test_result[model_name][task][test_class]['success'] != 0:
                            pass_at_k = self.cal_pass_at_k(
                                n, k, test_result[model_name][task][test_class]['success'])
                            success_num += pass_at_k
                        if test_result[model_name][task][test_class]['success'] + test_result[model_name][task][test_class]['partial_success'] != 0:
                            pass_at_k = self.cal_pass_at_k(
                                n, k, test_result[model_name][task][test_class]['success'] + test_result[model_name][task][test_class]['partial_success'])
                            partial_success_num += pass_at_k
                        sum_num += 1
                    except:
                        if test_result[model_name][task][test_class]['class_success'] != 0:
                            pass_at_k = self.cal_pass_at_k(
                                n, k, test_result[model_name][task][test_class]['class_success'])
                            class_success_num += pass_at_k
                        k_success = test_result[model_name][task][test_class]['class_success'] + \
                            test_result[model_name][task][test_class]['class_partial_success']
                        if k_success != 0:
                            pass_at_k = self.cal_pass_at_k(n, k, k_success)
                            partial_success_class_num += pass_at_k

            result[model_name] = {"fun_success": success_num / sum_num, "class_success": class_success_num / class_num,
                                  "fun_partial_success": partial_success_num / sum_num, "class_partial_success": partial_success_class_num / class_num}

        return result

    def tear_down(self):
        file_list = os.listdir()
        reserved_files = ["evaluation.py", "path_util.py", "test_pipeline.py", "README.md", "incremental generation.png", "run.sh"]
        for item in file_list:
            if item not in reserved_files and "test_pipeline" not in item and "_pycache__" not in item:
                if os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    os.remove(item)

