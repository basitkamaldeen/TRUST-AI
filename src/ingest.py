import json, time
from pathlib import Path

def save_raw_batch(records, out_dir="data/raw"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    filename = Path(out_dir) / f"batch_{int(time.time())}.jsonl"
    with open(filename, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
    print(f"✅ Saved raw batch: {filename}")

if __name__ == "__main__":
    # Example usage: simulate data ingestion
    sample_data = [{"text": "Example prompt-response pair"}]
    save_raw_batch(sample_data)
