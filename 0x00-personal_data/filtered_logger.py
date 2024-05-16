#!/usr/bin/env python3
"""Returns the log message obfuscated"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
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

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record by filtering sensitive fields"""
        # Get the original log message
        original_message = super(RedactingFormatter, self).format(record)
        # Filter the message
        filtered_message = filter_datum(
            self.fields, self.REDACTION, original_message, self.SEPARATOR)
        return filtered_message
