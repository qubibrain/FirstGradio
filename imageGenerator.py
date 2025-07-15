import gradio as gr
import os
from openai import OpenAI
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image
import base64

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        response_format="b64_json",
        size="1024x1024"
    )
    
    if not response.data or not response.data[0].b64_json:
        raise ValueError("No image data received from API")
    
    img_data = base64.b64decode(response.data[0].b64_json)
    img = Image.open(BytesIO(img_data))
    return img

with gr.Blocks(title="AI Image Generator") as demo:
    gr.Markdown("# 🎨 Prompt to Image Generator")
    gr.Markdown("Type in a creative prompt, and I'll visualize it for you!")

    with gr.Row():
        with gr.Column():
            prompt_input = gr.Textbox(label="Enter your prompt", placeholder="A sunset over the mountains...")
            generate_button = gr.Button("Generate Image")
        with gr.Column():
            image_output = gr.Image(label="Generated Image")

    generate_button.click(fn=generate_image, inputs=prompt_input, outputs=image_output)

if __name__ == "__main__":
    demo.launch()
