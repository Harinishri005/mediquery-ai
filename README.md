# MediQuery AI

**AI-powered medical report analyser that explains blood tests and lab results in plain English.**

Live Demo → https://mediquery-ai-x4nh.onrender.com  
GitHub → https://github.com/Harinishri005/mediquery-ai

---

## Problem

Most people receive blood test or lab reports and have no idea what the values mean. Doctors are too busy to explain everything. Existing tools like ChatGPT are too generic. MediQuery AI is built specifically for one purpose — making any medical report understandable to anyone, instantly.

---

## Solution

Upload a PDF medical report. Ask a question in plain English. Get a clear, simple AI-generated explanation in seconds — with automatic detection of abnormal values.

---

## Features

- PDF upload and text extraction
- AI powered plain English analysis
- Automatic abnormal value detection with red flags
- Query history saved with timestamps
- Responsible medical disclaimer on every result
- Clean responsive UI that works on mobile

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Flask |
| AI | Groq API — GPT-OSS 20B |
| PDF Processing | PyPDF2 |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Server | Gunicorn |
| Deployment | Render |
| Version Control | Git, GitHub |

---

## Screenshots

### Home Page
![Home Page](https://raw.githubusercontent.com/Harinishri005/mediquery-ai/main/static/images/home.png)

### Result Page
![Result Page](https://raw.githubusercontent.com/Harinishri005/mediquery-ai/main/static/images/result.png)

### History Page
![History Page](https://raw.githubusercontent.com/Harinishri005/mediquery-ai/main/static/images/history.png)

---

## Getting Started

### Prerequisites
- Python 3.10 or above
- Groq API key from console.groq.com

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Harinishri005/mediquery-ai.git
cd mediquery-ai
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment**

`GROQ_API_KEY=your_groq_api_key_here`

Get your free Groq API key at console.groq.com

**4. Run the application**
```bash
python app.py
```

**5. Open in browser**
http://127.0.0.1:5000

---

## Project Structure
mediquery/
├── static/
│   ├── images/
│   │   ├── home.png
│   │   ├── result.png
│   │   └── history.png
│   └── style.css
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── history.html
│   └── error.html
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md


---

## How it works

User uploads PDF
↓
PyPDF2 extracts text from report
↓
Text + question sent to Groq AI API
↓
AI generates plain English explanation
↓
Abnormal values detected and flagged
↓
Result displayed + saved to SQLite database


---

## What I learned

- Full stack web development with Python and Flask
- REST API integration with third party AI services
- PDF text extraction and processing
- SQL database design and CRUD operations
- Secure API credential management using environment variables
- Git version control and production deployment on Render
- Real world debugging — function naming conflicts, GitHub secret scanning, API model deprecations

---

## Roadmap

- User authentication with Flask-Login
- Support for scanned PDFs using Tesseract OCR
- Database migration from SQLite to PostgreSQL
- Multi-language support for regional Indian languages
- Email report summary feature

---

## Disclaimer

MediQuery AI is for informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified doctor for medical decisions.

---

**Built by Harinishri S**  
Medical Electronics Engineer → Software Developer  
Chennai, India
