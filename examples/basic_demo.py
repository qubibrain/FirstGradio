import gradio as gr

def reverse_text(text):
    """Simple function to reverse text"""
    return text[::-1] if text else ""

def count_words(text):
    """Count words in text"""
    if not text:
        return 0
    return len(text.split())

def analyze_sentiment(text):
    """Simple sentiment analysis (very basic)"""
    if not text:
        return "No text provided"
    
    positive_words = ["good", "great", "excellent", "amazing", "wonderful", "love", "happy"]
    negative_words = ["bad", "terrible", "awful", "hate", "sad", "disappointing"]
    
    text_lower = text.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    if positive_count > negative_count:
        return "Positive 😊"
    elif negative_count > positive_count:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Create the interface
with gr.Blocks(title="Basic Text Processing Demo") as demo:
    gr.Markdown("# 📝 Basic Text Processing Examples")
    gr.Markdown("Try out these simple text processing functions!")
    
    with gr.Tab("Text Reversal"):
        gr.Markdown("## Reverse Text")
        with gr.Row():
            with gr.Column():
                reverse_input = gr.Textbox(label="Enter text to reverse", placeholder="Type something...")
                reverse_button = gr.Button("Reverse Text")
            with gr.Column():
                reverse_output = gr.Textbox(label="Reversed text", interactive=False)
        
        reverse_button.click(reverse_text, inputs=reverse_input, outputs=reverse_output)
    
    with gr.Tab("Word Counter"):
        gr.Markdown("## Count Words")
        with gr.Row():
            with gr.Column():
                count_input = gr.Textbox(label="Enter text to count words", placeholder="Type a sentence...")
                count_button = gr.Button("Count Words")
            with gr.Column():
                count_output = gr.Number(label="Word count", interactive=False)
        
        count_button.click(count_words, inputs=count_input, outputs=count_output)
    
    with gr.Tab("Sentiment Analysis"):
        gr.Markdown("## Basic Sentiment Analysis")
        gr.Markdown("This is a very simple sentiment analyzer that looks for positive and negative words.")
        with gr.Row():
            with gr.Column():
                sentiment_input = gr.Textbox(label="Enter text for sentiment analysis", placeholder="How do you feel about this?")
                sentiment_button = gr.Button("Analyze Sentiment")
            with gr.Column():
                sentiment_output = gr.Textbox(label="Sentiment", interactive=False)
        
        sentiment_button.click(analyze_sentiment, inputs=sentiment_input, outputs=sentiment_output)

if __name__ == "__main__":
    demo.launch(share=False, debug=True) 