import sys
sys.path.insert(0, '.')

print('--- Verifying all modules ---')

from config import Config
print('[OK] config.py — UPLOAD_FOLDER:', Config.UPLOAD_FOLDER)

from utils.logger import logger
print('[OK] utils.logger')

from utils.pdf_parser import extract_text_from_pdf
from utils.docx_parser import extract_text_from_docx
print('[OK] utils.pdf_parser + utils.docx_parser')

from core.text_processor import TextProcessor
tp = TextProcessor()
cleaned = tp.clean_text('Hello! Python developer with 5 years experience in React.js and AWS.')
print('[OK] core.text_processor — sample:', cleaned[:60])

from core.skill_manager import SkillManager
sm = SkillManager('data/skills_db.json')
skills = sm.extract_skills('python django machine learning docker aws')
print('[OK] core.skill_manager — found skills:', skills)

from core.matcher import Matcher
m = Matcher()
score = m.calculate_score('python flask machine learning', 'python django machine learning')
analysis = m.analyze_skills(['python','machine learning'], ['python','django','machine learning'])
print('[OK] core.matcher — score:', score)
print('     matched:', analysis['matched_skills'])
print('     missing:', analysis['missing_skills'])

import app as flask_app
print('[OK] app.py — Flask app loaded cleanly')

print()
print('=== ALL MODULES VERIFIED SUCCESSFULLY ===')
