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
        """
        Creates session
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        self.session_id = uuid.uuid4()
        self.user_id_by_session_id[self.session_id] = user_id
        return self.session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the user ID associated with the given session ID.

        Parameters:
            session_id (str, optional): The session ID to retrieve the
            user ID for. Defaults to None.

        Returns:
            str: The user ID associated with the session ID,
            or None if the session ID is invalid or not found.
        """
        if session_id is None:
            return None
        user = self.user_id_by_session_id.get(session_id)
        return user
