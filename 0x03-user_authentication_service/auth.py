#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Converts password in to hash_password
    """
    byte = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte, bcrypt.gensalt())
    return hashed_password


def _generate_uuid() -> str:
    """
    Generate uuid
    """
    user_id = str(uuid.uuid4())
    return user_id


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user in the database
        Returns: User Object
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks and validates user password.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        user_password = user.hashed_password
        value = bcrypt.checkpw(password.encode('utf-8'), user_password)
        return value

    def create_session(self, email: str) -> str:
        """
        Session generator.
        """
        session_id = _generate_uuid()
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str):
        """
        Returns User object with session_id
        """
        user = self._db.find_user_by(session_id=session_id)
        if user:
            return user
        return None
