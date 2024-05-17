#!/usr/bin/env python3
"""Returns the log message obfuscated"""
import re
import logging
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter sensitive fields in the log message.

    Args:
        fields (List[str]): The list of fields to obfuscate.
        redaction (str): The string used to replace sensitive data.
        message (str): The log message containing the sensitive data.
        separator (str): The separator used in the log message.

    Returns:
        str: The log message with sensitive fields obfuscated.
    """
    for field in fields:
        message = re.sub(
            f"{field}=[^{separator}]*", f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """
    Creates and returns a logger named 'user_data' with a StreamHandler
    and a RedactingFormatter that logs up to logging.INFO level and does not
    propagate messages to other loggers.
    """
    # Create or retrieve the logger
    logger = logging.getLogger('user_data')

    # Set logging level to INFO
    logger.setLevel(logging.INFO)

    # Do not propagate messages to other loggers
    logger.propagate = False

    # Check if the logger already has handlers to avoid duplicate handlers
    if not logger.hasHandlers():
        # Create a console (stream) handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create and set the RedactingFormatter for the handler
        formatter = RedactingFormatter(
            PII_FIELDS, '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(console_handler)

    return logger
