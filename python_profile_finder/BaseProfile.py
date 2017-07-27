class BaseProfile:
    """
    A Users information that might be using a website. The following
        are the attributes (further can be added according to need):

    Attributes:
            name: Full name of the user
            email: Email address of user

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
