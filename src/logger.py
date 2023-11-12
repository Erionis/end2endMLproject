import logging
import os
from datetime import datetime

# create logs folder if not exists
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

# create log file path
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# create logger
logging.basicConfig(filename=LOG_FILE_PATH,
                    level=logging.INFO,
                    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s')

