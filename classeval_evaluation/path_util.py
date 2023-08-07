
import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
ROOT_DIR = str(Path(ROOT_DIR) / "..")
DATA_DIR = str(Path(ROOT_DIR) / "data")  # This is the data of this project
OUTPUT_DIR = str(Path(ROOT_DIR) / "output")  # This is the output of this project
LOGS_DIR = str(Path(ROOT_DIR) / "log")


class PathUtil:

    @staticmethod
    def orig_data_dir():
        path = Path(DATA_DIR)
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    @staticmethod
    def model_output_data(filename: str, ext: str):
        path = Path(OUTPUT_DIR)/'model_output'
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{filename}.{ext}'
        return str(path)
    
    @staticmethod
    def log_output_data(filename: str, ext: str):
        path = Path(LOGS_DIR)
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{filename}.{ext}'
        return str(path)

    @staticmethod
    def test_result_data(filename: str, ext: str):
        path = Path(OUTPUT_DIR)/'result'
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{filename}.{ext}'
        return str(path)

    @staticmethod
    def eval_data(dataset_name: str):
        path = Path(DATA_DIR)/f'{dataset_name}.json'
        return str(path)

    @staticmethod
    def benchmark_code_data(filename: str, ext: str):
        path = Path(DATA_DIR)/'benchmark_solution_code'
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{filename}.{ext}'
        return str(path)

    @staticmethod
    def benchmark_code_file():
        path = Path(DATA_DIR) / 'benchmark_solution_code'
        return str(path)

    @staticmethod
    def benchmark_test_file():
        path = Path(DATA_DIR) / 'benchmark_test_code'
        return str(path)

    @staticmethod
    def benchmark_test_data(filename: str, ext: str):
        path = Path(DATA_DIR)/'benchmark_test_code'
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{filename}.{ext}'
        return str(path)