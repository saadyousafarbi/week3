"""
Base classes for scraping websites.
"""
from exceptions import NotImplementedError


class BaseScraper:
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/55.0.2883.87 Safari/537.36'

    def __init__(self, username, password):
        """
        Contains all basic parameters required for scraping.

        Attributes:
            username (str) : Username credential of user
            password (str) : Password credential of user

        """
        self.username = username
        self.password = password

    @staticmethod
    def get_login_url(self):
        """
        Method constructs login url.
        """
        raise NotImplementedError

    @staticmethod
    def get_user_profile_url(self, login_session):
        """
        Retrieve profile url for logged in user.
        """
        raise NotImplementedError

    @staticmethod
    def login_user_and_get_session(self):
        """
        Login user and return request session.
        """
        raise NotImplementedError

    @staticmethod
    def login_and_retrieve_profile(self):
        """
        Method that performs login and also retrieves profile.
        Child class implementations are different depending on
        each child website.

        """
        raise NotImplementedError
