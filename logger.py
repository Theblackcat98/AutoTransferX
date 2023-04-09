import logging

class Logger:
    def __init__(self, log_file):
        # Initialize logging
        logging.basicConfig(filename=log_file, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

    def log(self, message):
        # Log the message
        self.logger.info(message)
