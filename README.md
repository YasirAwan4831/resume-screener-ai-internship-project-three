# AI Resume Screener & Job Matcher

A professional AI-powered tool developed in Python/Flask to automate resume screening and skill gap analysis.

## 🚀 Features
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

