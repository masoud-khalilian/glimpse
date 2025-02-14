import json
import pickle
import numpy as np
import pandas as pd

def convert_special_types(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, pd.DataFrame):
        return obj.to_dict(orient='records')
    elif isinstance(obj, pd.Series):
        return obj.to_dict()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def convert_pickle_to_json(pickle_file: str, json_file: str):
    """
    Convert a .pk pickle file into a .json file.

    :param pickle_file: Path to the input pickle file.
    :param json_file: Path to the output JSON file.
    """
    try:
        # Load the pickle file
        with open(pickle_file, 'rb') as f:
            data = pickle.load(f)

        # Convert and save to JSON
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False, default=convert_special_types)

        print(f"Successfully converted {pickle_file} to {json_file}")
    except Exception as e:
        print(f"Error converting {pickle_file} to JSON: {e}")

# Example usage
file_path = "./output/extractive_sentences-_-all_reviews_2017-_-none-_-2025-02-14-01-52-27-_-r3-_-rsa_reranked-google-pegasus-arxiv.pk"
convert_pickle_to_json(file_path, "data1.json")