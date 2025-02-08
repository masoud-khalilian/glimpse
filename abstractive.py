import os
import sys
import shutil
import argparse
from pathlib import Path
from glimpse.data_loading.generate_abstractive_candidates import main as generate_main
from glimpse.src.compute_rsa import main as rsa_main


def get_dataset_path():
    """Retrieve dataset path from command-line arguments or use default."""
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print(
            "Couldn't find a valid path. Using default path: data/processed/all_reviews_2017.csv"
        )
        return "data/processed/all_reviews_2017.csv"
    return sys.argv[1]


def check_cuda():
    """Check if CUDA is available."""
    if shutil.which("nvidia-smi") is None:
        print(
            "CUDA is not available. Please ensure CUDA is installed and the NVIDIA drivers are properly configured."
        )
        sys.exit(1)


def generate_summaries(dataset_path, add_padding=False):
    """Generate abstractive summaries using the model."""
    # args = argparse.Namespace(
    #     dataset_path=Path(dataset_path),
    #     scripted_run=True,
    #     no_trimming=add_padding,
    #     filter=None,  # If filtering isn't needed, keep it None
    #     model_name="google/pegasus-large",  # Default model (change as needed)
    #     device="cuda" if shutil.which("nvidia-smi") else "cpu",  # Auto-detect device
    #     output_dir="output",  # Default output directory
    # )

    return generate_main(dataset_path)  # Pass Namespace object


def compute_rsa_scores(summaries):
    print("Summaries path: ")
    print(Path(summaries))
    # """Compute RSA scores using the pre-trained model."""
    # args = argparse.Namespace(
    #     summaries=Path(summaries),
    #     model_name="google/pegasus-large",
    #     device="cuda" if shutil.which("nvidia-smi") else "cpu",
    #     output_dir="output",
    #     scripted_run=True,
    # )

    return rsa_main(Path(summaries))  # Pass Namespace object


def main():
    dataset_path = get_dataset_path()
    check_cuda()

    add_padding = "--add-padding" in sys.argv
    candidates = generate_summaries(dataset_path, add_padding)
    print(f"Generated summaries: {candidates}")
    rsa_scores = compute_rsa_scores(candidates)

    print(f"RSA Scores: {rsa_scores}")


if __name__ == "__main__":
    main()
