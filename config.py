import os

# Absolute path to the project root (where this file lives)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    # Storage paths resolved from project root — safe regardless of launch directory
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'storage', 'uploads')
    LOG_FILE      = os.path.join(BASE_DIR, 'storage', 'logs', 'app.log')

    ALLOWED_EXTENSIONS = {'pdf', 'docx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024   # 16 MB upload limit

    # Ensure critical directories exist on import
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
