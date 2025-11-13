from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import get_peft_config, get_peft_model, LoraConfig

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

lora_config = LoraConfig(r=8, lora_alpha=32, target_modules=["c_attn"], lora_dropout=0.1)
model = get_peft_model(model, lora_config)
# prepare hf datasets & Trainer
