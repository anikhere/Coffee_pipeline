import logging
import os
from datetime import datetime

# Create logs folder
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create log file with timestamp
log_file = f'log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
log_path = os.path.join(LOG_DIR, log_file)

# Setup logging ONCE
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s [%(name)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_path),      # Saves to file
        logging.StreamHandler()              # Prints to console
    ]
)

# Simple function to get logger
def get_logger(name):
    return logging.getLogger(name)