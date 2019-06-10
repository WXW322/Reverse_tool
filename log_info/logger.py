import logging

def get_logger(file_path, logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler(file_path)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger