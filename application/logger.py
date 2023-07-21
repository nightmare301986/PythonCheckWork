
import logging

logging.basicConfig(
    format='%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    handlers=[
        logging.FileHandler('notes_log.log', mode='a'),

    ],
    level=logging.INFO,
)
