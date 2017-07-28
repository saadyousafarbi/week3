"""
Base classes for user's profile.
"""
from exceptions import NotImplementedError


class BaseProfile:
    """
    A User profile information for a website.

    Attributes:
        name (str): Full name of the user
        email (str): Email address of user

    """
    def __init__(self, name, email):
        """
        Base Profile with basic profile information.
        """
        self.name = name
        self.email = email

    def print_user_profile(self):
        """
        Method that prints out all information regarding user profile.
        """
        raise NotImplementedError
