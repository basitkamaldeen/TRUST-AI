from transformers import pipeline
gen = pipeline("text-generation", model="models/exp1")
samples = ["Example prompt 1", "Example prompt 2"]
for s in samples:
    out = gen(s, max_new_tokens=100)
    print(out[0]["generated_text"])
