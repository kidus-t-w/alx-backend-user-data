#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Converts password in to hash_password
    """
    byte = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte, bcrypt.gensalt())
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers new user.

        Args:
            email (str): user email
            password (str): user password
        Returns:
            User object. If user exists valueError is raised
        """
        if self._db.find_user_by(email=email):
            raise ValueError("User {} already exists".format(email))
        hashed_password = _hash_password(password)
        user = User(email=email, hashed_password=hashed_password)
        self._db._session.add(user)
        self._db._session.commit()
        return user
