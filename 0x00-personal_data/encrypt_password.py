#!/usr/bin/env python3
"""Encodes password using hash table"""
import bcrypt


def hash_password(password):
    """
    A function to hash a password using bcrypt.

    Parameters:
        password (str): The password to be hashed.

    Returns:
        bytes: The hashed password.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')
