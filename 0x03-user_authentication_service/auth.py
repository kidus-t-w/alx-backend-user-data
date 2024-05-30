#!/usr/bin/env python3
""" Authentication Module """

import bcrypt
from db import DB
# from sqlalchemy.orm.exc import NoResultFound
# from typing import Union
# from user import User
# from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the passed password """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
