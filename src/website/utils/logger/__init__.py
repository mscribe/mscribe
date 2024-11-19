import sys
import os
import logging
import logging.handlers


LOGGER_FORMAT = logging.Formatter("%(asctime)s- %(levelname)s: %(message)s")


class Logger:
    def __init__(self, logger_name: str = None) -> None:
        self.logger_name = logger_name
        self.logger_path = os.path.join(sys.path[0],
                                        "logs",
                                        f"{logger_name}.log")

        handler = logging.handlers.TimedRotatingFileHandler(self.logger_path,
                                                            encoding="utf-8",
                                                            when="midnight",
                                                            interval=1,
                                                            backupCount=7)
        handler.setFormatter(LOGGER_FORMAT)
        self.logger = logging.getLogger(logger_name)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def info(self, message: str) -> None:
        """Log info message

        Args:
            message (str): logging message
        """
        self.logger.info(message)

    def error(self, message: str) -> None:
        """Log error message

        Args:
            message (str): logging message object
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """Log a creticial message

        Args:
            message (str): logging message object
        """
        self.logger.critical(message)

    def warning(self, message: str) -> None:
        """Log a warning message

        Args:
            message (str): logging message object
        """
        self.logger.warning(message)
