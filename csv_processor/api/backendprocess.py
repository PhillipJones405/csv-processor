import pandas as pd
import logging
import functools

logger = logging.getLogger('api.services')

def log_function_call(func):
    @functools.wrap(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        logger = logging.getLogger(__name__)
        logger.info(f"Calling {func.__qualname__}")
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        logger.info(f"{func.__qualname__} took {elapsed:.4f} seconds.")
        return result
    return wrapper

def process_this(filename):
    df = pd.read_csv(file)
    df['Processed'] = df['col1'] + df['col2']
    # Example processing: Add a new column
    df['Processed'] = df.sum(axis=1)