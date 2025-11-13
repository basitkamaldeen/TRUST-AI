from datasets import load_dataset
from transformers import AutoTokenizer

def tokenize_data(model_name="gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    ds = load_dataset("json", data_files="data/processed/clean.jsonl")["train"]
    def tokenize_fn(ex):
        return tokenizer(ex["text"], truncation=True, max_length=512)
    tok = ds.map(tokenize_fn, batched=True, remove_columns=["text"])
    tok.save_to_disk("data/processed/tokenized")
    print("✅ Tokenized dataset saved to disk")

if __name__ == "__main__":
    tokenize_data()
