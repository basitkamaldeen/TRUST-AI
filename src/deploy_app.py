import gradio as gr
from transformers import pipeline
pipe = pipeline("text-generation", model="username/trustai-model")
def chat(inp):
    return pipe(inp, max_new_tokens=128)[0]['generated_text']
gr.Interface(fn=chat, inputs="text", outputs="text").launch()
