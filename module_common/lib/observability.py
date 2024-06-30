from datetime import datetime
import logging
from functools import wraps
import time

logger = logging.getLogger(__name__)

def log_datetime(func):
    """Log the date and time of a function"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(
            f'Function: {func.__name__} Ended in {(end - start):.5f} milliseconds at {datetime.now()}'
        )        
        return result
    return wrapper