#!/usr/bin/env python3
"""
Basic Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Basic Authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for a given path.

        Args:
            path (str): The path for which authentication is being checked.
            excluded_paths (List[str]): A list of paths that are excluded
            from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request (flask.Request, optional): The request object.
            Defaults to None.

        Returns:
            str: The authorization header value,
            or None if the header is not present.
        """
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request.

        Args:
            request (flask.Request, optional): The request object.
            Defaults to None.

        Returns:
            TypeVar('User'): The current user object, or None if
            the user is not authenticated.
        """
        if request is None:
            return None
