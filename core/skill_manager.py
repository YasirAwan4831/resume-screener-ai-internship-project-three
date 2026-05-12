import json
import os
from utils.logger import logger


class SkillManager:
    """
    Loads a technical skills database (JSON) and extracts matching skills
    from a given text using single-word and bi-gram lookups.
    """

    def __init__(self, skills_db_path: str):
        # Resolve the path relative to the project root if it is not absolute
        if not os.path.isabs(skills_db_path):
            base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            skills_db_path = os.path.join(base, skills_db_path)

        self.skills_db_path = skills_db_path
        self.technical_skills = self._load_skills()
        logger.info(f"SkillManager loaded {len(self.technical_skills)} skills from DB.")

    # ------------------------------------------------------------------
    def _load_skills(self) -> set:
        try:
            with open(self.skills_db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return {s.lower() for s in data.get('technical_skills', [])}
        except FileNotFoundError:
            logger.error(f"Skills DB not found at: {self.skills_db_path}")
            return set()
        except Exception as exc:
            logger.error(f"Error loading skills DB: {exc}")
            return set()

    # ------------------------------------------------------------------
    def extract_skills(self, text: str) -> list:
        """
        Scans *text* for skills listed in the database.
        Checks individual words and consecutive bi-grams (e.g. 'machine learning').
        Returns a sorted, deduplicated list of matched skill names.
        """
        if not text:
            return []

        words = text.lower().split()
        found: set = set()

        for i, word in enumerate(words):
            # Single-word match
            if word in self.technical_skills:
                found.add(word)

            # Bi-gram match (look-ahead)
            if i < len(words) - 1:
                bi_gram = f"{word} {words[i + 1]}"
                if bi_gram in self.technical_skills:
                    found.add(bi_gram)

        return sorted(found)
