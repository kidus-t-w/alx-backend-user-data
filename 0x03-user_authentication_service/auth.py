#!/usr/bin/env python3
""" Authentication Module """

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from user import User
# from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the passed password """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initilizes db"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user in the database
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User {email} already exists')
