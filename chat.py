import gradio as gr

def chat(message, history):
    # Convert input to lowercase for case-insensitive matching
    user_input_lower = message.lower()
    
    if "hello" in user_input_lower or "hi" in user_input_lower:
        return "Hi there! What's on your mind?"
    elif "how are you" in user_input_lower:
        return "I'm just a program, but I'm functioning well!"
    elif "name" in user_input_lower:
        return "Dummy Chatbot: I am the Dummy Chatbot."
    elif "bye" in user_input_lower or "exit" in user_input_lower:
        return "Goodbye! Have a great day."
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

if __name__ == "__main__":
    gr.ChatInterface(chat, type="messages").launch()