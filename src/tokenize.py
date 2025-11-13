from datasets import load_dataset, Dataset
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
ds = load_dataset("json", data_files="data/processed/clean.jsonl")["train"]
def tokenize_batch(ex):
    return tokenizer(ex["text"], truncation=True, max_length=1024)
tok = ds.map(tokenize_batch, batched=True, remove_columns=["text"])
tok.save_to_disk("data/processed/tokenized_gpt2")
