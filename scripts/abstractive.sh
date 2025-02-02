#!/bin/bash

# Check if input file path is provided and valid
if [ -z "$1" ] || [ ! -f "$1" ]; then
    # if no path is provided, or the path is invalid, use the default test dataset
    echo "Couldn't find a valid path. Using default path: data/processed/all_reviews_2017.csv"
    dataset_path="data/processed/all_reviews_2017.csv"
else
    dataset_path="$1"
fi

# Activate the conda environment
# source ~/anaconda3/etc/profile.d/conda.sh
# conda activate "glimpse"

# Check if CUDA is available
if ! command -v nvidia-smi &> /dev/null; then
    echo "CUDA is not available. Please ensure CUDA is installed and the NVIDIA drivers are properly configured."
    exit 1
fi

# Generate abstractive summaries
# shellcheck disable=SC2199
if [[ "$@" =~ "--add-padding" ]]; then # check if padding argument is present
    # add '--no-trimming' flag to the script
    candidates=$(python glimpse/data_loading/generate_abstractive_candidates.py  --dataset_path "$dataset_path" --scripted-run --no-trimming | tail -n 1)
else
    # no additional flags
    candidates=$(python glimpse/data_loading/generate_abstractive_candidates.py --dataset_path "$dataset_path" --scripted-run | tail -n 1)
fi

# Compute the RSA scores based on the generated summaries
rsa_scores=$(python glimpse/src/compute_rsa.py --summaries $candidates | tail -n 1)

echo "RSA Scores: $rsa_scores"