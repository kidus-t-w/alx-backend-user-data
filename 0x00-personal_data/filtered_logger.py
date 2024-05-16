#!/usr/bin/env python3
import re
"""Returns the log message obfuscated"""


def filter_datum(fields, redaction, message, separator):
    for field in fields:
        pattern = f"{field}=[^{separator}]*"
        replacement = f"{field}={redaction}"
        message = re.sub(pattern, replacement, message)
    return message
