import threading
import globals
from utils import logger

def print_threads():
    globals.IM.pause_all()

    logger.info(15*'=' + ' Threads ' + 15*'=')
    for i, thread in enumerate(threading.enumerate()): 
        logger.info(f'[{i}] - {thread.name}')
    logger.info(39*'=')

    globals.IM.resume_all()