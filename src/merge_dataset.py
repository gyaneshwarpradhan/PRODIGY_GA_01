import json
from pathlib import Path

DATASET_DIR = Path("data/dataset_v2")
OUTPUT_FILE = Path("data/dataset_v3.json")

merged = []

for file in sorted(DATASET_DIR.glob("*.json")):
    print(f"Loading {file.name}...")
    with open(file, "r", encoding="utf-8") as f:
        merged.extend(json.load(f))

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)

print(f"\nMerged {len(merged)} records.")
print(f"Saved to {OUTPUT_FILE}")