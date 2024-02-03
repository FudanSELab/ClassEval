#!/bin/bash
folder_path="../output/model_output"

for file_path in "$folder_path"/*; do
    echo "$file_path"
    if [ -f "$file_path" ]; then
        file_name=$(basename "$file_path")

        file_name_no_extension="${file_name%.*}"
        echo "$file_name_no_extension"
        
        IFS="_" read -ra elements <<< "$file_name_no_extension"
        last_element="${elements[-1]}"

        if [[ $last_element == *"greedy"* ]]; then
            python evaluation.py --source_file_name "$file_name_no_extension" --eval_data ClassEval_data --greedy 1
        else
            python evaluation.py --source_file_name "$file_name_no_extension" --eval_data ClassEval_data --greedy 0
        fi
    fi
done
