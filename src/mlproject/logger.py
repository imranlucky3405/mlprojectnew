import logging
import os
from datetime import datetime

# Step 1: Create "logs" directory
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Step 2: Generate unique log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 3: Full path to the log file
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# Step 4: Configure logging AFTER defining LOG_FILE_PATH
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)