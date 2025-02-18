import json

import pandas as pd
import re

# Read the CSV file
df = pd.read_csv("./data/add_book_review_from_gpt_output.csv")

# Initialize a new dataframe
expanded_rows = []

for _, row in df.iterrows():
    summaries = re.findall(r"Summary \d+: (.+?)(?=Summary \d+:|$)", row["review/text"], re.DOTALL)
    for i, summary in enumerate(summaries, 1):
        expanded_rows.append({
            "id": row["id"],
            "title": row["title"],
            "review":summary.strip(),
            "text": row["review/text"],
            "metareview":row["metareview"]
        })

# Create a new DataFrame
expanded_df = pd.DataFrame(expanded_rows)

# Save to a new CSV file
expanded_df.to_csv("./data/cleaned_book_reviews.csv", index=False)

print("CSV file created successfully!")

# API Key (Replace with your actual key)
#
# key = "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"
# import pandas as pd
# import requests
# import json
# import time
#
# # File path
# input_file = "./data/add_book_review_from_gpt_output.csv"
# output_file = "./data/add_book_review_from_gpt_output.csv"
#
# # Read CSV file
# df = pd.read_csv(input_file)
#
# # Ensure metareview column exists
# if "metareview" not in df.columns:
#     df["metareview"] = None  # Create column if it doesn’t exist
#
#
# # Iterate over each row
# for index, row in df.iterrows():
#     # Skip rows that already have a metareview
#     if pd.notna(row["metareview"]):
#         print(f"Skipping row {index}, metareview already exists.")
#         continue
#
#     # Prepare the API request
#     review_text = row["review/text"]
#
#     if pd.isna(review_text) or review_text.strip() == "":
#         print(f"Skipping row {index}, review is empty.")
#         continue
#
#     print(f"Processing row {index}...")
#
#     response = requests.post(
#         url="https://openrouter.ai/api/v1/chat/completions",
#         headers={
#             "Authorization": f"Bearer {key}",
#             "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
#             "X-Title": "<YOUR_SITE_NAME>",  # Optional
#         },
#         data=json.dumps({
#             "model": "openai/gpt-4o",  # Optional
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": f"Summarize the following review into a concise general summary: {review_text}"
#                 }
#             ]
#         })
#     )
#
#     if response.status_code == 200:
#         try:
#             json_response = response.json()
#             metareview = json_response['choices'][0]['message']['content']
#             df.at[index, "metareview"] = metareview  # Store metareview in dataframe
#
#             # Save immediately to prevent data loss
#             df.to_csv(output_file, index=False)
#             print(f"Row {index} saved successfully.")
#
#         except json.JSONDecodeError as e:
#             print(f"Failed to parse JSON response for row {index}. Error: {e}")
#
#     else:
#         print(f"API Error {response.status_code} at row {index}: {response.text}")
#
#     # Small delay to avoid hitting API rate limits
#     time.sleep(1)  # Adjust as needed
#
# print("Processing completed. Final CSV saved.")
#
