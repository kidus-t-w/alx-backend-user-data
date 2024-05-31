#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Converts password in to hash_password
    """
    byte = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte, bcrypt.gensalt())
    return hashed_password
