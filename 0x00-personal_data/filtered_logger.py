#!/usr/bin/env python3
"""Returns the log message obfuscated"""
import re
import logging
from typing import List


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
