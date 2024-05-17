#!/usr/bin/env python3
"""Returns the log message obfuscated"""
import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector import Error, connection

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




def get_db() -> connection.MySQLConnection:
    """
    Returns a connector to a MySQL database.
    Uses environment variables for database credentials and configuration.
    """
    # Fetching credentials and database name from environment variables
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    if not db_name:
        raise ValueError("Database name must be set in the environment variable 'PERSONAL_DATA_DB_NAME'.")

    # Configuration dictionary for the database connection
    config = {
        'user': username,
        'password': password,
        'host': host,
        'database': db_name,
        'raise_on_warnings': True
    }

    try:
        # Establishing the database connection
        connection = mysql.connector.connect(**config)
        print("Successfully connected to the database.")
        return connection

    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Example usage
if __name__ == "__main__":
    conn = get_db()
    if conn:
        try:
            # Here you can perform database operations using the connection
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            for row in cursor.fetchall():
                print(row)
        finally:
            conn.close()  # Ensure the connection is closed when done
