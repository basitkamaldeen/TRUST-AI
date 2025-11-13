from transformers import AutoModelForCausalLM, TrainingArguments, Trainer, AutoTokenizer
from datasets import load_from_disk
from peft import LoraConfig, get_peft_model
import torch

def train(model_name="gpt2", output_dir="models/exp1"):
    ds = load_from_disk("data/processed/tokenized")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.resize_token_embeddings(len(tokenizer))

    # LoRA fine-tuning
    config = LoraConfig(r=8, lora_alpha=16, target_modules=["c_attn"], lora_dropout=0.1)
    model = get_peft_model(model, config)

    args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=1,
        per_device_train_batch_size=2,
        save_steps=500,
        logging_steps=100,
        fp16=torch.cuda.is_available(),
        report_to="none"
    )

    trainer = Trainer(model=model, args=args, train_dataset=ds)
    trainer.train()
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train()
