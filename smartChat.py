import gradio as gr
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # Make sure to set your OpenAI API key as environment variable
)

def chat(message, history):
    """
    Use OpenAI to generate intelligent responses instead of dummy responses
    """
    try:
        # Create a conversation with the user's input
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # You can change this to other models like gpt-4
            messages=[{"role": "system", "content": "You are a helpful and friendly AI assistant. Keep your responses concise and engaging."}]
            + history
            + [{"role": "user", "content": message}],
            max_tokens=150,  # Limit response length
            temperature=0.7  # Add some creativity to responses
        )
        
        content = response.choices[0].message.content
        return content.strip() if content else "I'm sorry, I couldn't generate a response."
    
    except Exception as e:
        # Fallback response if OpenAI API fails
        return f"I'm having trouble connecting to my brain right now. Error: {str(e)}"


if __name__ == "__main__":
    gr.ChatInterface(
            chat,
            type="messages",
            theme="ocean",
            textbox=gr.Textbox(
                placeholder="Chat with me! I'm powered by OpenAI and can help with various topics.", 
                container=False, 
                scale=7
            ),
            description="Ask me anything! I'm an AI assistant powered by OpenAI.",
            examples=[
                "What's the weather like today?", 
                "Can you help me with Python programming?", 
                "Tell me a joke",
                "What are the benefits of machine learning?"
            ],
            title="🎉 Smart AI Chatbot!"
        ).launch()