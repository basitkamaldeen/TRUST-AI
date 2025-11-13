from pathlib import Path
import json
def save_raw_batch(records, out_dir="data/raw"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    fn = Path(out_dir) / f"batch_{int(__import__('time').time())}.jsonl"
    with open(fn, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
    print("Saved", fn)
