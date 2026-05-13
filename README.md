<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a2744,100:0d47a1&height=200&section=header&text=AI%20Resume%20Screener&fontSize=48&fontColor=ffffff&fontAlignY=40&desc=Job%20Matcher%20%7C%20NLP%20Powered%20%7C%20Skill%20Gap%20Analysis&descAlignY=62&descSize=16&animation=fadeIn" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge\&logo=flask)
[![NLP](https://img.shields.io/badge/NLP-AI%20Powered-8A2BE2?style=for-the-badge&logo=openai&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-✓%20Completed-2ea44f?style=for-the-badge)]()
[![Internship](https://img.shields.io/badge/Nexe--Agent-Internship%20·%202026-7c3aed?style=for-the-badge)]()


--------


<br/>

A professional AI-powered Resume Screening and Job Matching application developed using **Python** and **Flask**.
The system automatically analyzes resumes, extracts technical skills using NLP techniques, compares them with job descriptions and generates intelligent match scoring with skill gap analysis.

<br/>

</div>

---

## 🔄 How It Works

```
Upload Resume
      ↓
Extract Resume Text
      ↓
Clean & Process Text
      ↓
Extract Technical Skills
      ↓
Compare With Job Description
      ↓
Calculate Match Percentage
      ↓
Generate Smart Analysis Report
```

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 📄 Resume Upload System
- PDF and DOCX format support
- Secure file handling & validation
- Drag & Drop upload interface

### 🧠 AI & NLP Processing
- Intelligent text preprocessing
- NLP-based normalization & cleaning
- Automated technical skill extraction

### 🎯 Job Matching Engine
- TF-IDF vectorization
- Cosine similarity scoring
- Real-time skill comparison

</td>
<td width="50%">

### 📊 Smart Match Analysis
- Match percentage generation
- Matched skills visualization
- Missing skills detection
- Candidate compatibility analysis

### 🎨 Premium UI Design
- Dark glassmorphism theme
- Responsive on all devices
- Smooth animations & interactions

### 🛡️ System Reliability
- Modular architecture
- Robust error handling
- Comprehensive logging system

</td>
</tr>
</table>

---

## 🛠️ Technology Stack

| Category | Technologies |
|:---|:---|
| **Backend** | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white&style=flat-square) |
| **AI / NLP** | ![NLTK](https://img.shields.io/badge/-NLTK-4B8BBE?style=flat-square) ![SpaCy](https://img.shields.io/badge/-SpaCy-09A3D5?style=flat-square) ![Scikit--learn](https://img.shields.io/badge/-Scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=flat-square) |
| **Similarity** | ![TF-IDF](https://img.shields.io/badge/-TF--IDF-8A2BE2?style=flat-square) ![Cosine](https://img.shields.io/badge/-Cosine%20Similarity-6A0DAD?style=flat-square) |
| **Parsing** | ![pdfplumber](https://img.shields.io/badge/-pdfplumber-E44D26?style=flat-square) ![python-docx](https://img.shields.io/badge/-python--docx-2B579A?style=flat-square) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white&style=flat-square) ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white&style=flat-square) ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black&style=flat-square) |
| **Testing** | ![Testing](https://img.shields.io/badge/-Python%20Test%20Utils-2ea44f?style=flat-square) |

---

## 📂 Project Structure

```
resume-screener-ai/
│
├── 🧩 core/
│   ├── matcher.py           ← Resume & JD matching engine
│   ├── skill_manager.py     ← Skill extraction & management
│   └── text_processor.py   ← NLP preprocessing & cleaning
│
├── 🗄️ data/
│   └── skills_db.json       ← Skills knowledge base
│
├── 🎨 static/
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── upload.js
│   └── icon.jpeg
│
├── 📦 storage/
│   ├── logs/
│   └── uploads/
│
├── 🖥️ templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
│
├── 🧪 tests/
│   ├── test_nlp.py
│   └── verify_all.py
│
├── 🔧 utils/
│   ├── docx_parser.py
│   ├── logger.py
│   └── pdf_parser.py
│
├── app.py                   ← Main Flask application
├── config.py                ← Configuration settings
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites
```
Python 3.11+  |  pip  |  Git
```

---

### Step 1 — Clone Repository
```bash
git clone https://github.com/your-username/resume-screener-ai.git
cd resume-screener-ai
```

### Step 2 — Create Virtual Environment
```bash
# Create
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Linux / Mac
source venv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run Application
```bash
python app.py
```

### Step 5 — Open in Browser
```
http://127.0.0.1:5000
```

---

### 🧪 Run Tests
```bash
python tests/verify_all.py
```

---

## 🧩 Core Modules

| Module | Purpose |
|:---|:---|
| `matcher.py` | Resume & Job Description similarity matching |
| `skill_manager.py` | Skill extraction, parsing & management |
| `text_processor.py` | NLP preprocessing, normalization & cleaning |
| `pdf_parser.py` | PDF resume parsing via pdfplumber |
| `docx_parser.py` | DOCX resume parsing via python-docx |
| `logger.py` | Application-wide structured logging |

---

## 📈 Roadmap

```
Current  ████████████████████  ✅ v1.0 Complete
```

| Feature | Status |
|:---|:---:|
| Multi-resume batch comparison | 🔜 Planned |
| ATS scoring system | 🔜 Planned |
| AI-powered recommendations | 🔜 Planned |
| Database integration | 🔜 Planned |
| Admin dashboard | 🔜 Planned |
| OpenAI / Gemini integration | 🔜 Planned |
| Resume ranking system | 🔜 Planned |

---

## ✅ Project Status

```
✅  Completed          All core features implemented
✅  Fully Tested       NLP pipeline verified & stable
✅  GitHub Ready       Clean, documented codebase
✅  Portfolio Project  Built during Nexe-Agent Internship
```

---

## 🔥 Key Highlights

- 🤖 **AI-Based Resume Screening** — NLP skill detection pipeline
- 🏗️ **Modular Architecture** — Clean, scalable Python backend
- 🎯 **Real-World Concept** — Solves actual HR automation problems
- 📱 **Responsive Frontend** — Works on all screen sizes
- 🔬 **TF-IDF + Cosine Similarity** — Proven NLP matching technique
- 📦 **Production Ready** — Error handling, logging, testing included

---

<div align="center">

## 👨‍💻 Developer

Develop By [**Muhammad Yasir**](https://yasirawan4831.github.io/futuristic-links-dashboard/)

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-0d47a1?style=for-the-badge&logo=google-chrome&logoColor=white)](https://yasirawan4831.github.io/futuristic-links-dashboard/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YasirAwan4831)

*Built with ❤️ during the **Nexe-Agent** AI & Automation Internship · 2026*

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d47a1,50:1a2744,100:0d1117&height=120&section=footer&animation=twinkling" width="100%"/>

⭐ **If you found this useful, please star the repository!** ⭐

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yasir.resume-screener&left_color=0d1117&right_color=0d47a1)
&nbsp;
![Made with Love](https://img.shields.io/badge/Made%20with-❤️%20by%20Yasir-red?style=flat-square)
&nbsp;
![Nexe-Agent](https://img.shields.io/badge/Nexe--Agent-AI%20Automation-7c3aed?style=flat-square)

</div>

-----