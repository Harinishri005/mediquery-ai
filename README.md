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

Create a `.env` file in the root directory:
