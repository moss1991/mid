import sys
from datetime import datetime
from loguru import logger

def getLogger():
    now_datetime_str    = datetime.now().strftime("%Y-%m-%d")
    logger.add(sys.path[0]+"/logs/runtime_"+now_datetime_str+".log", rotation="4:00", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
    return logger

    
logger = getLogger()