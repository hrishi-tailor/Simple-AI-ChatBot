# Simple AI Chatbot

An interactive AI-driven chatbot designed to showcase the core principles of Natural Language Processing (NLP), intent recognition, and adaptive learning. This project demonstrates the fundamental components needed to create intelligent conversational agents.

## 🔧 Technical Highlights

- **Intent Recognition**: Utilizes fuzzy string matching (via RapidFuzz) to efficiently map user inputs to predefined patterns.
- **Dynamic Knowledge Base**: Implements real-time augmentation of the intents dataset through JSON serialization and deserialization.
- **Natural Language Understanding (NLU)**: Employs lexical and semantic similarity techniques to enhance conversational accuracy.
- **Error Handling**: Features robust fallback mechanisms to manage unmatched inputs, enabling conversational learning.
- **State Management**: Optimizes interaction flow for real-time response generation.

## 🚀 Scaling Toward ChatGPT-like Models

This project serves as a foundation for developing advanced AI conversational systems, such as ChatGPT, by offering hands-on experience in:

### Key Learnings:
- **Intent Classification**: Demonstrates how user queries are interpreted, echoing principles found in transformer-based models like GPT for multi-intent recognition.
- **Dynamic Knowledge Augmentation**: Simulates continual learning with real-time dataset updates, crucial for adaptive systems.
- **Core NLP Workflows**: Provides practical exposure to tokenization, similarity detection, and response generation—essential for pre-training and fine-tuning transformer models.
- **Conversational Context Management**: Introduces techniques for handling conversational states and user feedback loops.
- **Scalability**: The modular design lays the groundwork for incorporating neural networks, transformers, or APIs to expand the chatbot’s capabilities.

Mastering these concepts bridges the gap between basic conversational agents and sophisticated systems like OpenAI's ChatGPT. 🚀

## 🛠️ How to Run

To run the chatbot on your local machine, follow these simple steps:

# Chatbot Setup Instructions

### 1. Clone the repository
To start, clone this repository to your local machine. You can do this by running the following command in your terminal or command prompt:
```console
git clone https://github.com/hrishi-tailor/Simple-AI-ChatBot.git
```
### 2. Install dependencies
After cloning the repository, navigate to the project folder where the repository is located. You can install the required dependencies by running:

```console
pip install -r requirements.txt
```
This command will install all the necessary Python packages specified in the requirements.txt file, which are needed to run the chatbot.

### 3. Run the chatbot
To run the chatbot, you need to execute the script that starts the chatbot. You can do this by running:
```console
python chat.py
```
This will launch the chatbot, and it should start processing your commands.

### 4. Start chatting
Once the chatbot is running, you can begin interacting with it directly in the terminal. Simply type your questions, and if the chatbot doesn’t know the answer, you can help it learn by providing additional input in real-time.

## 📜 License
This project is licensed under the MIT License.
