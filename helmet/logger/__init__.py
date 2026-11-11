
import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler


# Explicit project root directory
ROOT_DIR = r"C:\Users\USER\DataScience\Bio-Tech\Detectron_and_YOLO\Helmet-Detection"

# Generate unique timestamp
TIMESTAMP = datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")

# Create logs directory OUTSIDE helmet
LOG_DIR = os.path.join(ROOT_DIR, "logs", TIMESTAMP)

MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3

# Create directory
os.makedirs(LOG_DIR, exist_ok=True)

# Log file path
LOG_FILE = os.path.join(LOG_DIR, f"{TIMESTAMP}.log")


logging.basicConfig(
    level=logging.DEBUG,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(
            LOG_FILE,
            maxBytes=MAX_LOG_SIZE,
            backupCount=BACKUP_COUNT,
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ],
    force=True
)

