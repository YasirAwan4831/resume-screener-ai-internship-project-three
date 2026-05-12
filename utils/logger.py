import logging
import os

# Resolve log file path relative to the project root (not cwd at import time)
_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(_BASE_DIR, 'storage', 'logs', 'app.log')


def setup_logger():
    """
    Configures and returns the application-wide logger.
    Creates the log directory if it does not already exist.
    """
    # Ensure the directory exists before opening the file handler
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    logger = logging.getLogger('ResumeScreener')

    # Avoid adding duplicate handlers on repeated imports
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # File handler — full debug level
    fh = logging.FileHandler(LOG_FILE, encoding='utf-8')
    fh.setLevel(logging.DEBUG)

    # Console handler — info level only
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


logger = setup_logger()
