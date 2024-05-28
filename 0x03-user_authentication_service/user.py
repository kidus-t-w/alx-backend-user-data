#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String


class User():
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
    
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)
