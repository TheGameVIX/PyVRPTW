import logging

def setup_logger():
    # Create a custom logger
    logger = logging.getLogger(__name__)

    # Set the level of logger
    logger.setLevel(logging.ERROR)

    # Create handlers
    file_handler = logging.FileHandler('log.txt')
    file_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)

    return logger

def log_error(logger, error_message):
    logger.error(error_message)