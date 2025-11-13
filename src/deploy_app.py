import gradio as gr
from transformers import pipeline

pipe = pipeline("text-generation", model="your-username/trustai-model")

def chat(prompt):
    res = pipe(prompt, max_new_tokens=100)
    return res[0]["generated_text"]

app = gr.Interface(fn=chat, inputs="text", outputs="text", title="TrustAI Chatbot")
app.launch()
