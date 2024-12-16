# AI Study Assistant 📚

An intelligent study companion powered by Google's Gemini AI that helps students master complex topics through interactive learning. The application provides detailed explanations, generates practice questions, and offers topic-specific guidance.

## Features ✨

- **Topic Understanding**: Get detailed, easy-to-understand explanations of complex topics
- **Practice Questions**: Generate subject-specific practice questions with solutions
- **Interactive Learning**: Engage with concepts through an interactive Q&A interface
- **Subject-Specific Focus**: Tailored explanations based on the academic subject
- **Animated UI**: Modern, responsive interface with smooth animations

## Tech Stack 🛠️

- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Backend**: Flask (Python)
- **AI Integration**: Google Gemini API
- **Deployment**: Gunicorn
- **Styling**: Tailwind CSS

## Prerequisites 📋

- Python 3.8 or higher
- Google Gemini API key
- Modern web browser
- Internet connection

## Installation 💻

1. **Clone the repository**
```bash
git clone https://github.com/prabOG7/ai-study-assistant.git
cd ai-study-assistant
```

2. **Install dependencies**
```bash
pip install flask google-generativeai flask-cors gunicorn
```

3. **Set up environment variables**
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

4. **Run the application**
```bash
python app.py
```

The application will be available at `http://localhost:8000`

## Deployment 🚀

### Deploying to Render

1. Create a Render account at [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure the service:
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Add your `GOOGLE_API_KEY` to environment variables
6. Deploy!

## Usage 📝

1. Open the application in your web browser
2. Enter your study topic or concept
3. Choose the type of help you need:
   - Detailed explanation
   - Practice questions
   - Interactive learning
4. Review the AI-generated content and engage with the interactive elements

## Project Structure 📁

```
ai-study-assistant/
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Main HTML template
├── requirements.txt      # Python dependencies
└── README.md            # Documentation
```

## Contributing 🤝

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Environment Variables 🔑

- `GOOGLE_API_KEY`: Your Google Gemini API key

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments 🙏

- Google Gemini API for powering the AI capabilities
- Flask framework for the backend
- Tailwind CSS for the styling
- All contributors and users of this application

---

Made with ❤️ for students everywhere
@prabOG7
