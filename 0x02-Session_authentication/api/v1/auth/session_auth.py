#!/usr/bin/env python3
"""
Session Authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Session Authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if user_id is None or type(user_id) != str:
            return None
        self.session_id = uuid.uuid4()
        self.user_id_by_session_id[self.session_id] = user_id
        return self.session_id
