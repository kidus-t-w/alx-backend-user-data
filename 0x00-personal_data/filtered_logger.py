import re
"""Returns the log message obfuscated"""


def filter_datum(fields, redaction, message, separator):
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]*", f"{field}={redaction}", message)
    return message
