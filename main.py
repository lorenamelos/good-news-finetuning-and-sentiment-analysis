import json

# Function to load JSON data from a file
def load_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Path to your JSON file
json_file_path = "dataset.json"

# Load JSON data from file
good_headlines = load_json_file(json_file_path)
print(len(good_headlines))
print(good_headlines)
