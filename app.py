import gradio as gr

def get_response(img_path, text_prompt):
    # Mock LLM response
    return f"Mock response for prompt: '{text_prompt}' with file: '{img_path}'"

def handle_input(file, prompt):
    if file is None or prompt.strip() == "":
        return "Please upload a file and enter a prompt."
    return get_response(file, prompt)

with gr.Blocks() as demo:
    gr.Markdown("## 💬 Face LLM Demo (Prototype)")

    with gr.Row():
        file_input = gr.File(label="Upload Image or Video", type="filepath")
        prompt_input = gr.Textbox(label="Text Prompt", placeholder="Enter your question...")
    
    submit_btn = gr.Button("Submit")
    output = gr.Textbox(label="Model Response")

    submit_btn.click(fn=handle_input, inputs=[file_input, prompt_input], outputs=output)

demo.launch()
