import gradio as gr
import numpy as np
from PIL import Image

def greet(name):
    """Simple text processing function"""
    return f"Hello {name}! Welcome to Gradio!"

def calculate_square(number):
    """Simple mathematical function"""
    return number ** 2

def process_image(image):
    """Simple image processing function"""
    if image is not None:
        # Convert to PIL Image if it's not already
        if isinstance(image, np.ndarray):
            image = Image.fromarray(image)
        
        # Simple processing: convert to grayscale
        gray_image = image.convert('L')
        return gray_image
    return None

def generate_random_data():
    """Generate random data for visualization"""
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    return x, y

# Create the Gradio interface
with gr.Blocks(title="FirstGradio - Learning Examples") as demo:
    gr.Markdown("# 🎉 Welcome to FirstGradio!")
    gr.Markdown("This is a learning project to explore Gradio capabilities.")
    
    with gr.Tab("Text Processing"):
        gr.Markdown("## Text Processing Example")
        with gr.Row():
            with gr.Column():
                name_input = gr.Textbox(label="Enter your name", placeholder="Type your name here...")
                greet_button = gr.Button("Greet Me!")
            with gr.Column():
                greet_output = gr.Textbox(label="Greeting", interactive=False)
        
        greet_button.click(greet, inputs=name_input, outputs=greet_output)
    
    with gr.Tab("Mathematics"):
        gr.Markdown("## Mathematical Operations")
        with gr.Row():
            with gr.Column():
                number_input = gr.Number(label="Enter a number", value=5)
                square_button = gr.Button("Calculate Square")
            with gr.Column():
                square_output = gr.Number(label="Result", interactive=False)
        
        square_button.click(calculate_square, inputs=number_input, outputs=square_output)
    
    with gr.Tab("Image Processing"):
        gr.Markdown("## Image Processing Example")
        with gr.Row():
            with gr.Column():
                image_input = gr.Image(label="Upload an image")
                process_button = gr.Button("Convert to Grayscale")
            with gr.Column():
                image_output = gr.Image(label="Processed Image")
        
        process_button.click(process_image, inputs=image_input, outputs=image_output)
    
    with gr.Tab("Data Visualization"):
        gr.Markdown("## Data Visualization Example")
        with gr.Row():
            plot_button = gr.Button("Generate Random Data")
            plot_output = gr.Plot(label="Random Sine Wave with Noise")
        
        plot_button.click(generate_random_data, outputs=plot_output)

if __name__ == "__main__":
    demo.launch(share=False, debug=True) 