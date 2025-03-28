import gradio as gr
from llm_interface import get_response

def handle_input(file, prompt):
    if file is None or prompt.strip() == "":
        return "Please upload a file and enter a prompt."
    return get_response(file, prompt)

with gr.Blocks() as demo:
    gr.Markdown("Face LLM Demo (Prototype)")

    file_input = gr.File(label="Upload Image or Video", type="filepath")
    prompt_input = gr.Textbox(label="Text Prompt", placeholder="Ask something...")

    submit = gr.Button("Submit")
    output = gr.Textbox(label="Model Response")

    submit.click(fn=handle_input, inputs=[file_input, prompt_input], outputs=output)

demo.launch()