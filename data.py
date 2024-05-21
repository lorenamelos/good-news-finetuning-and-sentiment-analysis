import json
from sklearn.model_selection import train_test_split


# CREATING TRAIN AND TEST DATA:

# Load the dataset from JSON
with open("dataset.json", "r") as f:
    dataset = json.load(f)

# Separate texts and labels
texts = [example["text"] for example in dataset]
labels = [example["label"] for example in dataset]

# Split the dataset into training and testing sets
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=0.2, random_state=42, stratify=labels)

# Create training dataset
train_dataset = [{"text": text, "label": label} for text, label in zip(train_texts, train_labels)]

# Create testing dataset
test_dataset = [{"text": text, "label": label} for text, label in zip(test_texts, test_labels)]

# Save the datasets to JSON files
with open("train_dataset.json", "w") as f:
    json.dump(train_dataset, f, indent=4)

with open("test_dataset.json", "w") as f:
    json.dump(test_dataset, f, indent=4)

print("Datasets created successfully!")


# CREATING HUGGINGFACE DICT DATA:

from datasets import DatasetDict, Dataset

# Load JSON files
train_file = "train_dataset.json"
test_file = "test_dataset.json"

# Load datasets
train_data = Dataset.from_json(train_file)
test_data = Dataset.from_json(test_file)

# Combine datasets into a DatasetDict
headline_news = DatasetDict({"train": train_data, "test": test_data})

print("DatasetDict created successfully!")

# If you want to see the structure of the combined dataset, you can print its keys and sizes
print("\nKeys of the combined dataset:")
print(headline_news.keys())

print("\nSizes of the datasets:")
for key, dataset in headline_news.items():
    print(f"{key}: {len(dataset)} examples")
