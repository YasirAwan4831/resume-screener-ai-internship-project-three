from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Matcher:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def calculate_score(self, resume_text, jd_text):
        """
        Calculates cosine similarity score between resume and job description.
        Returns a percentage score.
        """
        if not resume_text or not jd_text:
            return 0.0
            
        tfidf_matrix = self.vectorizer.fit_transform([resume_text, jd_text])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        
        score = float(similarity[0][0]) * 100
        return round(score, 2)

    def analyze_skills(self, resume_skills, jd_skills):
        """
        Compares skills and identifies matches and missing requirements.
        """
        resume_set = set([s.lower() for s in resume_skills])
        jd_set = set([s.lower() for s in jd_skills])
        
        matched_skills = list(resume_set.intersection(jd_set))
        missing_skills = list(jd_set - resume_set)
        
        return {
            "matched_skills": sorted(matched_skills),
            "missing_skills": sorted(missing_skills)
        }
