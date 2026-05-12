import unittest
from core.text_processor import TextProcessor
from core.skill_manager import SkillManager
import os

class TestNLP(unittest.TestCase):
    def setUp(self):
        self.processor = TextProcessor()
        # Mock paths for testing
        self.skills_path = os.path.join('data', 'skills_db.json')
        self.skill_manager = SkillManager(self.skills_path)

    def test_text_cleaning(self):
        raw_text = "Python developer with 5+ years experience in React.js and AWS!!!"
        cleaned = self.processor.clean_text(raw_text)
        self.assertIn("python", cleaned)
        self.assertNotIn("!!!", cleaned)

    def test_skill_extraction(self):
        text = "Experienced in python, django and machine learning"
        skills = self.skill_manager.extract_skills(text)
        self.assertIn("python", skills)
        self.assertIn("django", skills)
        self.assertIn("machine learning", skills)

if __name__ == '__main__':
    unittest.main()
