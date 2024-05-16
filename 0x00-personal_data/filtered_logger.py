#!/usr/bin/env python3
"""Returns the log message obfuscated"""
import re


def filter_datum(fields, redaction, message, separator):
    """Returns the log message obfuscated."""
    for field in fields:
        message = re.sub(
            f"{field}=[^{separator}]*", f"{field}={redaction}", message)
    return message
