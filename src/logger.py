## logging the data

import logging ## any execution should be logged to track.
import os
from datetime import datetime

# Create logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Build timestamped logfile path
LOG_FILE = datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
filename=LOG_FILE_PATH,
level=logging.INFO,
format="%(asctime)s | %(levelname)s | %(name)s:%(lineno)d | %(message)s",
datefmt="%Y-%m-%d %H:%M:%S",
)

##test
'''if __name__ == "__main__":
  logging.info("Logging has started.")
'''
# this is also one time 


