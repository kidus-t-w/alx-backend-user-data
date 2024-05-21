#!/usr/bin/env python3
"""Basic Authentication
"""
from api.v1.auth.auth import Auth


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
