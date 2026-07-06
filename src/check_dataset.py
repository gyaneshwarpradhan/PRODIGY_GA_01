from utils import load_dataset

data = load_dataset("data/dataset.json")

print("=" * 50)
print("Total Records:", len(data))
print("=" * 50)
print(data[0])