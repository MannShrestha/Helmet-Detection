from helmet.logger import logging,ROOT_DIR, LOG_DIR, LOG_FILE
# ------------------------------------------------------------------------------
# Initialize Logging
# ------------------------------------------------------------------------------

# logging.info("Logging initialized successfully")
# logging.info(f"Project root: {ROOT_DIR}")
# logging.info(f"Log directory: {LOG_DIR}")
# logging.info(f"Log file: {LOG_FILE}")

# print("PROJECT ROOT:", ROOT_DIR)
# print("LOG DIRECTORY:", LOG_DIR)
# print("LOG FILE:", LOG_FILE)
import sys
from helmet.logger import logging
from helmet.exception import HelmetException


try:
    a = 10
    b = 0

    result = a / b

except Exception as e:
    logging.error("An exception occurred")
    raise HelmetException(e, sys)