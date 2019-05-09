import logging

def get_logger(file_path):
    logger = logging.getLogger()
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler(file_path)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger