from transformers import pipeline

def evaluate(model_path="models/exp1"):
    gen = pipeline("text-generation", model=model_path)
    test_prompts = [
        "Explain what artificial intelligence is:",
        "Write a poem about trust in technology:",
    ]
    for prompt in test_prompts:
        print(f"\n🧩 Prompt: {prompt}")
        print("Response:", gen(prompt, max_new_tokens=80)[0]['generated_text'])

if __name__ == "__main__":
    evaluate()
