import logging


class Logger:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Create handler for writing log messages to a file
        file_handler = logging.FileHandler(".\\logs\\automation_exercise.log")
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler to print log messages on the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and apply it to handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
