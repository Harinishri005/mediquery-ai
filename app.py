from flask import Flask, render_template, request
import PyPDF2
import io
import requests
import re
from database import init_db, save_query, get_all_queries

app = Flask(__name__, static_folder='static')

from dotenv import load_dotenv
import os
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def show_result():
    question = request.form["question"]
    report = request.files["report"]

    # Extract text from PDF
    # Extract text from PDF
    # Extract text from PDF
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(report.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        if not text.strip():
            return render_template("error.html", message="Could not extract text from this PDF. Please make sure it is a text-based PDF and not a scanned image.")
    except Exception as e:
        return render_template("error.html", message="Invalid file uploaded. Please upload a valid PDF file only.")
    # Send to Groq AI
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + GROQ_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful medical assistant. Explain medical reports in simple plain English. Always advise consulting a doctor for medical decisions."
                },
                {
                    "role": "user",
                    "content": "Here is my medical report:\n" + text + "\n\nMy question is: " + question
                }
            ]
        }
    )

    data = response.json()
    answer = data["choices"][0]["message"]["content"]

    # Format answer
    answer = answer.replace("**", "<strong>", 1)
    while "**" in answer:
        answer = answer.replace("**", "</strong>", 1)
        if "**" in answer:
            answer = answer.replace("**", "<strong>", 1)
    answer = answer.replace("\n", "<br>")

    # Detect abnormal values from report text
    normal_ranges = {
        "blood sugar": (70, 100),
        "fasting blood sugar": (70, 100),
        "hemoglobin": (12, 16),
        "heart rate": (60, 100),
        "cholesterol": (0, 200),
        "creatinine": (0.6, 1.2),
    }

    flags = []
    for parameter, (low, high) in normal_ranges.items():
        pattern = parameter + r"[^\d]*(\d+\.?\d*)"
        matches = re.findall(pattern, text.lower())
        for match in matches:
            value = float(match)
            if value < low or value > high:
                flags.append(f"{parameter.title()}: {value} (Normal: {low}-{high})")

    has_abnormal = len(flags) > 0

    # Save to database
    save_query(question, answer)

    return render_template("result.html",
        question=question,
        answer=answer,
        has_abnormal=has_abnormal,
        flags=flags)

@app.route("/history")
def history():
    queries = get_all_queries()
    return render_template("history.html", queries=queries)

if __name__ == "__main__":
    app.run(debug=True)