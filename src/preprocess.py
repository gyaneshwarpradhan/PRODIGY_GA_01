import json
from datasets import Dataset
from transformers import GPT2Tokenizer

# Load JSON
with open("data/dataset.json", "r", encoding="utf-8") as f:
    records = json.load(f)

texts = []

for item in records:
    texts.append(
        f"""### Instruction:
{item['instruction']}

### Response:
{item['response']}"""
    )

dataset = Dataset.from_dict({"text": texts})

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token


def tokenize(example):
    encoding = tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=256,
    )

    encoding["labels"] = encoding["input_ids"].copy()

    return encoding


tokenized_dataset = dataset.map(
    tokenize,
    batched=True,
    remove_columns=["text"]      # <-- IMPORTANT
)

tokenized_dataset.save_to_disk("data/tokenized")

print(tokenized_dataset)