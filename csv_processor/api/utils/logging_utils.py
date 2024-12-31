import functools
import logging
import time

logger = logging.getLogger('api.services')

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        logger.info(f"Calling {func.__qualname__}")
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        logger.info(f"{func.__qualname__} took {elapsed:.4f} seconds.")
        return result
    return wrapper