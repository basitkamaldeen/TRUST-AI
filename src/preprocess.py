import json, re
from pathlib import Path

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def preprocess(in_dir="data/raw", out_file="data/processed/clean.jsonl"):
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    with open(out_file, "w") as out:
        for file in Path(in_dir).glob("*.jsonl"):
            for line in open(file):
                record = json.loads(line)
                text = clean_text(record.get("text", ""))
                if len(text) > 5:
                    out.write(json.dumps({"text": text}) + "\n")
    print(f"✅ Cleaned data saved to {out_file}")

if __name__ == "__main__":
    preprocess()
