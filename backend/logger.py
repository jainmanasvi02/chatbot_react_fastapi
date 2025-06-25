import logging
from logging.handlers import RotatingFileHandler
import os

# Ensure logs directory exists
os.makedirs("backend/logs", exist_ok=True)

# Logger setup
logger = logging.getLogger("backend_logger")
logger.setLevel(logging.INFO)

# File handler with rotation
file_handler = RotatingFileHandler("backend/logs/errors.log", maxBytes=1_000_000, backupCount=3)
file_handler.setLevel(logging.ERROR)

# Console handler (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatters
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Attach handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)


