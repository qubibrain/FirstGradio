import gradio as gr

def dummy_chat(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()
    
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

def chat(message, history):
    return dummy_chat(message)


if __name__ == "__main__":
    force_dark_mode = """,
    <script>
        const url = new URL(window.location);,
        if (url.searchParams.get('__theme') !== 'dark') {,
            url.searchParams.set('__theme', 'dark');,
            window.location.href = url.href;,
        },
    </script>
    """
    js_code = """
<script>
    console.log("Custom JavaScript loaded with ChatInterface!");
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
</script>
"""
    with gr.Blocks(head=js_code) as demo:
        gr.ChatInterface(chat,
        type="messages",
        chatbot=gr.Chatbot(height=300, type="messages"),
        theme="ocean",
        textbox=gr.Textbox(placeholder="Chat with me, I can only respond to simple questions.", container=False, scale=7),
        description="Ask Dummy Chatbot any question",
        examples=["Hello", "How are you?", "What is your name?"],
        title="Dummy Chatbot")

    demo.launch()