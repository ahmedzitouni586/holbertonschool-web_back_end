#!/usr/bin/env python3
"""Auth module"""

from typing import List
from flask import request

class Auth:
    """Auth class"""
    def __init__(self) -> None:
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if the path is not in the list of strings excluded_paths.
        """
        if path is None or excluded_paths is None or not(excluded_paths):
            return True
        ret = True
        for excluded_path in excluded_paths:
            if excluded_path == path:
                ret = False
            elif excluded_path[-1] == '/':
                s = excluded_path.rstrip(excluded_path[-1])
                if s == path:
                    ret = False
            elif path[-1] == '/':
                s = path.rstrip(path[-1])
                if s == excluded_path:
                    ret = False
        return ret

    def authorization_header(self, request=None) -> str:
        """
        If request doesn't contain the header key Authorization, returns None
        Otherwise, return the value of the header request Authorization
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return None. request will be the Flask request object.
        """
        return None
