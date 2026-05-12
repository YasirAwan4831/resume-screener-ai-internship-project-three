# AI Resume Screener & Job Matcher

A professional AI-powered tool developed in Python/Flask to automate resume screening and skill gap analysis.

##  Features
- **Smart Parsing**: Support for PDF and DOCX formats.
- **NLP Processing**: Advanced text cleaning and normalization using NLTK.
- **Skill Extraction**: Automated technical skill detection from a custom knowledge base.
- **Match Scoring**: Cosine similarity matching using TF-IDF vectorization.
- **Premium UI**: Modern dark-themed dashboard with responsive design.


## 🛠️ Technology Stack
- **Backend**: Python, Flask
- **NLP**: NLTK, Scikit-learn, SpaCy
- **Parsers**: pdfplumber, python-docx
- **Frontend**: HTML5, CSS3 (Glassmorphism), JavaScript

## Folder Strucuute 
```
resume-screener-ai/
├─ __pycache__/
│  ├─ app.cpython-314.pyc
│  └─ config.cpython-314.pyc
├─ core/
│  ├─ __pycache__/
│  │  ├─ __init__.cpython-314.pyc
│  │  ├─ matcher.cpython-314.pyc
│  │  ├─ skill_manager.cpython-314.pyc
│  │  └─ text_processor.cpython-314.pyc
│  ├─ __init__.py
│  ├─ matcher.py
│  ├─ skill_manager.py
│  └─ text_processor.py
├─ data/
│  └─ skills_db.json
├─ static/
│  ├─ assets/
│  ├─ css/
│  │  └─ main.css
│  └─ js/
│     └─ upload.js
├─ storage/
│  ├─ logs/
│  └─ uploads/
│     ├─ jane_smith_resume.docx
│     ├─ john_doe_resume.docx
│     ├─ m-cv.pdf
│     └─ resume.pdf
├─ templates/
│  ├─ base.html
│  ├─ index.html
│  └─ result.html
├─ tests/
│  ├─ __init__.py
│  ├─ test_nlp.py
│  └─ verify_all.py
├─ utils/
│  ├─ __pycache__/
│  │  ├─ __init__.cpython-314.pyc
│  │  ├─ docx_parser.cpython-314.pyc
│  │  ├─ logger.cpython-314.pyc
│  │  └─ pdf_parser.cpython-314.pyc
│  ├─ __init__.py
│  ├─ docx_parser.py
│  ├─ logger.py
│  └─ pdf_parser.py
├─ .gitignore
├─ app.py
├─ config.py
├─ README.md
└─ requirements.txt
```


## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd resume-screener-ai
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the App**:
   Open `http://127.0.0.1:5000` in your browser.

## 📂 Project Structure
- `core/`: NLP logic and matching algorithms.
- `utils/`: File parsers and logging.
- `storage/`: Uploaded files and application logs.
- `templates/`: Premium HTML layouts.
- `static/`: Custom CSS and visual assets.

