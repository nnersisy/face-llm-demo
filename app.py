# app.py
import gradio as gr
import time
from llm_interface import get_response

def handle_input(file, prompt):
    if file is None or prompt.strip() == "":
        yield "Please upload a file and enter a prompt."
        return

    full_response = get_response(file, prompt)
    streamed = ""
    for char in full_response:
        streamed += char
        yield streamed
        time.sleep(0.02)

def show_preview(file):
    if file is None:
        return gr.update(visible=False), gr.update(visible=False)

    file_ext = file.split(".")[-1].lower()
    if file_ext in ["png", "jpg", "jpeg", "gif"]:
        return gr.update(value=file, visible=True), gr.update(visible=False)
    elif file_ext in ["mp4", "mov", "avi", "webm"]:
        return gr.update(visible=False), gr.update(value=file, visible=True)
    else:
        return gr.update(visible=False), gr.update(visible=False)

with gr.Blocks() as demo:
    gr.Markdown("Face LLM Demo (Streaming + Media Preview)")

    file_input = gr.File(label="Upload Image or Video", type="filepath")

    with gr.Row():
        image_preview = gr.Image(label="Image Preview", visible=False, scale=0.2)
        video_preview = gr.Video(label="Video Preview", visible=False, scale=0.2)

    prompt_input = gr.Textbox(label="Text Prompt", placeholder="Ask something...")
    submit = gr.Button("Submit")
    output = gr.Textbox(label="Model Response", lines=6)

    file_input.change(fn=show_preview, inputs=[file_input], outputs=[image_preview, video_preview])
    submit.click(fn=handle_input, inputs=[file_input, prompt_input], outputs=output)

demo.launch()
