# 🚀 ATS Resume Scorer

An AI-powered Applicant Tracking System (ATS) Resume Scorer that analyzes resumes against job descriptions, calculates ATS compatibility, identifies missing skills, and provides AI-generated recommendations to improve resume quality.

---

## 📌 Overview

ATS Resume Scorer is a full-stack web application that helps job seekers evaluate how well their resumes match a specific job description before applying.

The application extracts text from resumes, compares it with the provided job description using NLP and semantic similarity techniques, calculates an ATS compatibility score, highlights missing keywords and skills, and generates personalized AI suggestions for improving the resume. Users can also export detailed analysis reports as PDF.

---

## ✨ Features

* 📄 Upload resumes in PDF format
* 📝 Paste or upload job descriptions
* 🤖 AI-powered resume analysis
* 📊 ATS compatibility score
* 🎯 Skill matching and gap analysis
* 🔍 Keyword extraction
* 📈 Semantic similarity scoring
* 💡 AI-generated resume improvement suggestions
* 📑 Download detailed PDF reports
* 🔐 User authentication with Supabase
* 📂 Resume analysis history

---

## 🛠️ Tech Stack

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* FastAPI
* Python

### Authentication & Database

* Supabase

### AI / NLP

* spaCy
* Sentence Transformers
* RapidFuzz
* NumPy

### PDF Processing

* PyMuPDF (fitz)
* WeasyPrint

---

## 📁 Project Structure

```
ATS_SCORER/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── utils/
│   ├── models/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── assets/
│   ├── pages/
│   └── streamlit_app.py
│
├── reports/
├── uploads/
├── static/
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/harshiroy/ATS_SCORER.git
```

```bash
cd ATS_SCORER
```

---

### 2. Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Linux/macOS

```bash
python3 -m venv .venv
```

---

### 3. Activate the Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure Environment Variables

Create a `.env` file in the project root and add:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key

GROQ_API_KEY=your_groq_api_key

SECRET_KEY=your_secret_key
```

> Never commit your `.env` file or API keys to GitHub.

---

## ▶️ Running the Application

### Start the Backend

```bash
python -m uvicorn backend.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### Start the Frontend

```bash
streamlit run streamlit_app.py
```

Frontend runs at:

```
http://localhost:8501
```

---

## 📖 How It Works

1. User signs in securely using Supabase.
2. Upload a resume in PDF format.
3. Paste the target job description.
4. The backend extracts resume text.
5. NLP models analyze keywords and semantic similarity.
6. The system calculates an ATS score.
7. Missing skills and keywords are identified.
8. AI generates actionable improvement suggestions.
9. Users can download a detailed PDF report.

---

## 📊 ATS Score Components

* Resume–Job Description similarity
* Skills matched
* Missing skills
* Keyword coverage
* Experience relevance
* Education relevance
* AI-generated recommendations

---

## 📦 Key Dependencies

* FastAPI
* Uvicorn
* Streamlit
* Supabase
* spaCy
* Sentence Transformers
* RapidFuzz
* NumPy
* PyMuPDF
* WeasyPrint
* python-dotenv

---

## 📸 Screenshots

Add screenshots of:

* Login Page
* Dashboard
* Resume Upload
* ATS Score
* Missing Skills
* AI Suggestions
* PDF Report

Example:

```
screenshots/
├── login.png
├── dashboard.png
├── upload.png
├── ats_score.png
├── suggestions.png
```

---

## 🔮 Future Enhancements

* Multi-resume comparison
* Resume version tracking
* Support for DOCX resumes
* Industry-specific ATS scoring
* Interview question generation
* Cover letter generation
* Resume templates
* Analytics dashboard
* Recruiter mode

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature-name
```

3. Commit your changes:

```bash
git commit -m "Add new feature"
```

4. Push to your branch:

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Harshita Roy**

Artificial Intelligence & Data Science Student

GitHub: https://github.com/harshiroy

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
