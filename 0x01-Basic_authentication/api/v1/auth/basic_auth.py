#!/usr/bin/env python3
"""Basic Authentication
"""
import base64
import binascii
from api.v1.auth.auth import Auth
from typing import Tuple
from models.user import User


class BasicAuth(Auth):
    """Basic Authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the base64 authorization header from the
        given authorization header string.

        Args:
            authorization_header (str): The authorization header string.

        Returns:
            str: The extracted base64 authorization header, or
            None if the header is not valid.
        """
        if type(authorization_header) == str:
            header = authorization_header.split()
            if len(header) == 2:
                basic = header[0] + " "
                authorization = header[1]
                if basic == "Basic ":
                    return authorization
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a base64 authorization header string into a decoded string.

        Args:
            base64_authorization_header (str): The base64
            encoded authorization header string.

        Returns:
            str: The decoded string if the base64 authorization
            header is valid, None otherwise.

        Raises:
            None
        """
        if type(base64_authorization_header) != str:
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user credentials from the decoded base64
        authorization header.

        Parameters:
            decoded_base64_authorization_header (str): The decoded
            base64 authorization header.

        Returns:
            tuple: A tuple containing the username and password
            extracted from the authorization header.
                   Returns None if the authorization header is
                   not in the correct format.
        """
        if type(decoded_base64_authorization_header) == str:
            if ":" in decoded_base64_authorization_header:
                credentials = decoded_base64_authorization_header.split(":", 1)
                value = (credentials[0], credentials[1])
                return value
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
        Get user Object based on user's email and password

        Parameters:
            user_email (str): The email of the user.
            user_pwd (str): The password of the user.

        Returns:
            User
        """
        if isinstance(user_email, str) and isinstance(user_pwd, str):
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user based on the
        authorization header in the request.

        Args:
            request (flask.Request, optional): The request object.
            Defaults to None.

        Returns:
            TypeVar('User'): The user object corresponding to the
            provided credentials, or None if the credentials are invalid.
        """
        authentication_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(authentication_header)
        authentication_token = self.decode_base64_authorization_header(b64_auth_token)
        credentials = self.extract_user_credentials(authentication_token)
        return self.user_object_from_credentials(*credentials)
