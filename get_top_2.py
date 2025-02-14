import pandas as pd


def get_top_2_indices(file_path):
    """
    Reads a CSV file and returns all rows corresponding to index values 0 and 1.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing all rows with index values 0 and 1.
    """
    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("The CSV file is empty.")

    # Ensure first column contains the index values
    index_column = df.columns[0]  # Assuming the first column represents the index values

    # Select rows where the first column has values 0 or 1
    top_2_df = df[df[index_column].isin([0, 1])]

    # Save to CSV
    top_2_df.to_csv("./top_2_indices.csv", index=False)

    return top_2_df


# Example usage
file_path = "./data/candidates/extractive_sentences-_-all_reviews_2020-_-none-_-2025-02-13-16-11-57.csv"
top_2_rows = get_top_2_indices(file_path)
print(top_2_rows)
