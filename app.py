# app.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config={
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 40,
        "max_output_tokens": 2048,
    }
)

# Initialize chat history
chat = model.start_chat(history=[])

# Set up the educational system prompt
SYSTEM_PROMPT = """You are an educational assistant designed to help students learn. 
Focus on clear explanations, step-by-step solutions, and encouraging critical thinking.
Break down complex concepts and provide relevant examples."""

# Send initial system prompt
chat.send_message(SYSTEM_PROMPT)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        question = data.get('question')
        subject = data.get('subject', '')

        if subject:
            formatted_question = f"[Subject: {subject}] {question}"
        else:
            formatted_question = question

        response = chat.send_message(formatted_question)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
