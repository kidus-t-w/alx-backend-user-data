#!/usr/bin/env python3
"""Basic Authentication
"""
import base64
import binascii
from api.v1.auth.auth import Auth
from typing import Tuple


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
                credentials = decoded_base64_authorization_header.split(":")
                value = (credentials[0], credentials[1])
                return value

        return None
