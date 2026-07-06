# MediQuery AI

A web application that analyses medical reports and answers health questions in plain English using AI.

## Problem it solves
Most people receive blood test or lab reports and have no idea what the values mean. MediQuery AI lets anyone upload a medical report, ask a question, and get a clear plain English explanation instantly.

## Features
- Upload any PDF medical report
- Ask questions in plain English
- AI powered analysis using Groq API
- Automatically flags abnormal values
- Saves query history with timestamps
- Responsible medical disclaimer

## Tech Stack
- **Backend** — Python, Flask
- **AI** — Groq API (Llama 3.3)
- **PDF Processing** — PyPDF2
- **Database** — SQLite
- **Frontend** — HTML, CSS, JavaScript

## How to run locally

1. Clone the repository
2. Install dependencies
3. Add your Groq API key to .env file
4. Run the app

```bash
pip install flask pypdf2 requests python-dotenv
python app.py
```

## Screenshots
Home page — clean upload form with AI analysis
Result page — plain English explanation with abnormal value detection
History page — all past queries saved with timestamps