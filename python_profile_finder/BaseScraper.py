class BaseScraper:

    def __init__(self, base_url, username, password):
        """
        Contains all basic parameters required for scraping.

        Attributes:
            base_url (str) : Base URL provided by user of website
            username (str) : Username credential of user
            password (str) : Password credential of user

        """
        self.base_url = base_url
        self.username = username
        self.password = password

    @staticmethod
    def login_and_retrieve_profile(self):
        """
        Method that performs login and also retrieves profile.
        Child class implementations are different depending on
        each child website.

        """
