#!/usr/bin/env python3
"""DB module
"""
import logging

from typing import Dict
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User

logging.disable(logging.WARNING)
class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def add_user(self, email: str, hashed_password: str) -> User:
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user
    
    def find_user_by(self, **kwargs: Dict[str, str]) -> User:
        """Find a user by specified attributes.

        Raises:
            error: NoResultFound: When no results are found.
            error: InvalidRequestError: When invalid query arguments are passed

        Returns:
            User: First row found in the `users` table.
        """
        column = User.__table__.columns
        if kwargs is None:
            raise InvalidRequestError
        for key in kwargs:
            if key not in column:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).one()
        if user is None:
            raise NoResultFound
        return user
    
    def update_user(self, user_id: int, **kwargs) -> None:
        user = self.find_user_by(id=user_id)
        if user is None:
            raise ValueError
        user = self._session.query(user)
        