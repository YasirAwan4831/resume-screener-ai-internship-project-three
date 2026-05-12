import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already present
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        """
        Cleans the extracted text: lowercasing, removing non-alphanumeric chars,
        removing extra whitespace, and filtering stopwords.
        """
        if not text:
            return ""
            
        # Lowercase
        text = text.lower()
        
        # Remove URLs
        text = re.sub(r'http\S+\s*', ' ', text)
        
        # Remove RT and cc
        text = re.sub(r'RT|cc', ' ', text)
        
        # Remove hashtags and mentions
        text = re.sub(r'#\S+', '', text)
        text = re.sub(r'@\S+', '  ', text)
        
        # Remove punctuations
        text = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]', ' ', text)
        
        # Remove non-ascii characters
        text = re.sub(r'[^\x00-\x7f]', r' ', text)
        
        # Remove extra whitespaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove stopwords
        words = text.split()
        words = [w for w in words if w not in self.stop_words]
        
        return " ".join(words)
