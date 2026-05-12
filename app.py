"""
app.py — Main Flask entry point for the AI Resume Screener application.
"""

import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

from config import Config
from utils.logger import logger
from utils.pdf_parser import extract_text_from_pdf
from utils.docx_parser import extract_text_from_docx
from core.text_processor import TextProcessor
from core.skill_manager import SkillManager
from core.matcher import Matcher

# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.config.from_object(Config)

# ---------------------------------------------------------------------------
# Component initialisation (done once at startup)
# ---------------------------------------------------------------------------
text_processor = TextProcessor()
skill_manager  = SkillManager(os.path.join('data', 'skills_db.json'))
matcher        = Matcher()

logger.info("Resume Screener AI — application started.")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def allowed_file(filename: str) -> bool:
    """Returns True when *filename* has a permitted extension."""
    return (
        '.' in filename
        and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS
    )


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    # --- Validate file presence -----------------------------------------
    if 'resume' not in request.files:
        flash('No file part in the request. Please select a resume file.', 'error')
        return redirect(url_for('index'))

    resume_file = request.files['resume']
    jd_text     = request.form.get('job_description', '').strip()

    if resume_file.filename == '':
        flash('No file selected. Please choose a PDF or DOCX resume.', 'error')
        return redirect(url_for('index'))

    if not jd_text:
        flash('Job description cannot be empty. Please paste the JD text.', 'error')
        return redirect(url_for('index'))

    if not allowed_file(resume_file.filename):
        flash('Unsupported file type. Only PDF and DOCX files are accepted.', 'error')
        return redirect(url_for('index'))

    # --- Save uploaded file ---------------------------------------------
    filename = secure_filename(resume_file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    resume_file.save(filepath)
    logger.info(f"Resume uploaded: {filename}")

    # --- Extract raw text -----------------------------------------------
    ext = filename.rsplit('.', 1)[1].lower()
    if ext == 'pdf':
        raw_text = extract_text_from_pdf(filepath)
    else:
        raw_text = extract_text_from_docx(filepath)

    if not raw_text:
        flash('Could not extract text from the resume. The file may be corrupted or image-based.', 'error')
        return redirect(url_for('index'))

    logger.info(f"Text extracted — {len(raw_text)} characters.")

    # --- NLP pipeline ---------------------------------------------------
    clean_resume = text_processor.clean_text(raw_text)
    clean_jd     = text_processor.clean_text(jd_text)

    resume_skills = skill_manager.extract_skills(clean_resume)
    jd_skills     = skill_manager.extract_skills(clean_jd)

    match_score    = matcher.calculate_score(clean_resume, clean_jd)
    skill_analysis = matcher.analyze_skills(resume_skills, jd_skills)

    logger.info(
        f"Analysis complete — score: {match_score}% | "
        f"matched: {len(skill_analysis['matched_skills'])} | "
        f"missing: {len(skill_analysis['missing_skills'])}"
    )

    # --- Render result page ---------------------------------------------
    results = {
        'filename'           : filename,
        'score'              : match_score,
        'matched_skills'     : skill_analysis['matched_skills'],
        'missing_skills'     : skill_analysis['missing_skills'],
        'total_resume_skills': len(resume_skills),
        'total_jd_skills'    : len(jd_skills),
    }
    return render_template('result.html', results=results)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
