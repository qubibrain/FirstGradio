# FirstGradio - Gradio Learning Project

This project is created to learn and experiment with Gradio, a Python library for creating customizable web interfaces for machine learning models.

If you want a more detailed explanation of the code here, please visit my blog at [Beyond the Prompt: Designing AI Experiences with Gradio](https://www.qubibrain.ai/blog/first_gradio)

## 🎯 Project Goals

- Learn Gradio fundamentals and best practices
- Experiment with different types of Gradio interfaces
- Build interactive demos for machine learning models
- Understand how to deploy Gradio applications

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd FirstGradio
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Setting Up OpenAI API Token

To use OpenAI features in this project, you need to set up your OpenAI API token:

1. Get your OpenAI API key:
   - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key or use an existing one

2. Create a `.env` file in the project root:
```bash
touch .env
```

3. Add your OpenAI API key to the `.env` file:
```bash
echo "OPENAI_API_KEY=your_api_key_here" >> .env
```

**Important Security Notes:**
- Never commit your `.env` file to version control
- Replace `your_api_key_here` with your actual OpenAI API key
- Keep your API key secure and don't share it publicly

### Running the Application

To run a Gradio app:
```bash
python app.py
```

The application will be available at `http://localhost:7860` by default.

## 📁 Project Structure

```
FirstGradio/
├── README.md
├── requirements.txt
├── app.py
├── examples/
│   └── basic_demo.py
└── models/
    └── (your ML models here)
```

## 🧪 Learning Examples

This project includes various examples to help you learn Gradio:

### Basic Examples
- **Text Input/Output**: Simple text processing demos
- **Image Processing**: Image classification and manipulation
- **Audio Processing**: Audio file handling and processing
- **Data Visualization**: Charts and graphs with Gradio

### Advanced Examples
- **Custom Components**: Building custom Gradio components
- **State Management**: Handling application state
- **API Integration**: Connecting to external APIs
- **Model Deployment**: Deploying ML models with Gradio

## 📚 Resources

- [Gradio Documentation](https://gradio.app/docs/)
- [Gradio Examples](https://gradio.app/gallery)
- [Gradio GitHub Repository](https://github.com/gradio-app/gradio)

## 🤝 Contributing

This is a learning project, but feel free to:
- Add new examples
- Improve existing code
- Share your learnings and insights

## 📝 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🎓 Learning Path

1. **Start with Basic Interfaces**: Text, image, and audio inputs/outputs
2. **Explore Components**: Buttons, sliders, dropdowns, etc.
3. **Build Interactive Demos**: Create engaging user experiences
4. **Deploy Your Apps**: Learn about hosting and deployment
5. **Advanced Features**: Custom components, state management, etc.

---

Happy learning with Gradio! 🎉 