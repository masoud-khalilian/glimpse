import sys
import shutil
from pathlib import Path
from glimpse.data_loading.generate_extractive_candidates import main as generate_main
from glimpse.src.compute_rsa import main as rsa_main


class Config:
    def __init__(self):
        self.database_path = "data/processed/all_reviews_2017.csv"
        self.limit = 10

    def get_database_path(self):
        return self.database_path

    def get_limit(self):
        return self.limit



def check_cuda():
    """Check if CUDA is available."""
    if shutil.which("nvidia-smi") is None:
        print(
            "CUDA is not available. Please ensure CUDA is installed and the NVIDIA drivers are properly configured."
        )
        sys.exit(1)


def generate_extractive(config):

    return generate_main(config.get_database_path(), config.get_limit())  # Pass Namespace object


def compute_rsa_scores(summaries):
    print("Summaries path: ",Path(summaries))
    return rsa_main(Path(summaries))  # Pass Namespace object


def main():
    config = Config()
    check_cuda()
    candidates = generate_extractive(config)
    print("now computing rsa scores")
    print("now computing rsa scores")
    print("now computing rsa scores")
    compute_rsa_scores(candidates)

    # print(f"RSA Scores: {rsa_scores}")


if __name__ == "__main__":
    main()
