import argparse
from inference_pipeline import InferencePipeline

def args_init():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path",
        type=str,
        default="../data/ClassEval_data.json",
        help="ClassEval data",
    )
    parser.add_argument(
        "--greedy",
        type=int,
        default=1,
        help="Whether to generate model results with greedy strategy",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="model_output.json",
        help="output file path",
    )
    parser.add_argument(
        "--cuda",
        type=int,
        nargs="+",  # Accept one or more integers
        default=None,
        help="List of CUDA device(s), default value is None. If not set, use all available devices.",
    )
    parser.add_argument(
        "--generation_strategy",
        type=int,
        default=0,
        help="Holistic = 0, Incremental = 1, Compositional = 2",
    )
    parser.add_argument(
        "--model",
        type=int,
        default=1,
        help="Instruct_CodeGen = 0, WizardCoder = 1, Instruct_StarCoder = 2, InCoder = 3, \
        PolyCoder = 4, SantaCoder = 5, Vicuna = 6, ChatGLM = 7, GPT_3_5 = 8, GPT_4 = 9, others = 10, \
        Magicoder = 11, CodeGeeX2 = 12, DeepSeekCoder_inst = 13, Gemini_Pro = 14, CodeLlama_13b_inst = 15",
    )
    parser.add_argument(
        "--checkpoint",
        type=str,
        default="WizardLM/WizardCoder-15B-V1.0",
        help="checkpoint of the model",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="temperature value in generation config",
    )
    parser.add_argument(
        "--max_length",
        type=int,
        default=2048,
        help="max length of model's generation result",
    )
    parser.add_argument(
        "--openai_key",
        type=str,
        default="openai_key",
        help="need openai key if use GPT-3.5 or GPT-4",
    )
    parser.add_argument(
        "--openai_base",
        type=str,
        default="openai_base",
        help="need openai base if use GPT-3.5 or GPT-4",
    )

    parser.add_argument(
        "--google_api_key",
        type=str,
        default="google_api_key",
        help="need google api key if use Gemini Pro",
    )

    parser.add_argument(
        "--sample",
        type=int,
        default=5,
        help="The number of code samples that are randomly generated for each task.",
    )
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = args_init()
    infer = InferencePipeline(args)
    infer.pipeline()