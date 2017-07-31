import requests

from bs4 import BeautifulSoup

from BaseScraper import BaseScraper


class ZameenScraper(BaseScraper):
    base_url = 'https://www.zameen.com'
    headers_data = {
        'Referer': 'https://www.zameen.com/login.html',
        'User-Agent': BaseScraper.user_agent,
    }

    def __init__(self, username, password):
        """
        Extends base class BaseScraper.

        Attributes:
            base_url (str) : Base URL provided by user of website
            username (str) : Username credential of user
            password (str) : Password credential of user
            login_url (str): Zameen's URL for logging in derived from base URL
            profile_url (str) : Zameen's static url containing profile

        """
        self.username = username
        self.password = password
        self.login_url = self.get_login_url()
        self.profile_url = self.get_profile_url()

    def get_login_url(self):
        """
        Method constructs login url.
        """
        login_url = '{base_url}/login.html'.format(base_url=self.base_url)
        return login_url

    @classmethod
    def get_profile_url(self):
        """
        Method returns profile url for login form.
        """
        user_profile_url = 'http://profolio.zameen.com/profolio/'
        return user_profile_url

    def login_user_and_get_session(self):
        """
        A function that uses the objects username and password and
        retrieves Zameen profile information.

        Arguments:
            self

        :return:
            returns an object containing all available information on
            profile and also prints it

        """
        session = requests.Session()
        login_data = {
            'email': self.username,
            'password': self.password,
            'keep' : 'keep',
            'submit': 1,
            'action_login': 1,
        }
        print self.login_url
        response = session.post(self.login_url, data=login_data, headers=self.headers_data)
        if 'Logged in' in response.text:
            print 'Login successful for the user: {}'.format(self.username)
            return session
        return None

    def get_user_profile_url(self, login_session):
        """
        Retrieve profile url for logged in user.

        Arguments:
            login_session (session): A session with user logged in

        Returns:
            profile_url (str): A url string of the users profile

        """
        response = login_session.get(self.profile_url, headers=self.headers_data)
        soup = BeautifulSoup(response.content, 'html.parser')
        extracted_profile_link = soup.findAll('a', href=True, text='My Account & Profiles')
        extracted_profile_link = extracted_profile_link[0]['href']
        user_profile_url = ('{profile_url}/{user_profile_url}').format(
            profile_url=self.profile_url,user_profile_url=extracted_profile_link,
        )
        return user_profile_url

    def extract_user_profile_data(self, login_session, profile_url):
        """
        Returns a Pakwheels user profile information.

        Arguments:
            login_session (session): logged in session of the user
            profile_url (str): url of the users profile

        Returns:
            Returns a dictionary object containing profile info of user

        """
        profile_info = login_session.get(profile_url, headers=self.headers_data).text
        soup = BeautifulSoup(profile_info, 'html.parser')
        user_email = soup.find('input', {'id': 'email'}).get('value')
        user_name = soup.find('input', {'id': 'contact'}).get('value')
        user_phone_number = soup.find('input', {'id': 'phone_country_0'}).get('value')
        user_phone_number += soup.find('input', {'id': 'phone_area_0'}).get('value')
        user_phone_number += soup.find('input', {'id': 'phone_0'}).get('value')
        user_country = soup \
            .find('select', {'id': 'country'}) \
            .find('option', selected=True) \
            .text
        user_address = soup.find('input', {'id': 'address'}).get('value')
        return {
            'user_name': user_name,
            'user_email': user_email,
            'user_phone_number': user_phone_number,
            'user_address': user_address,
            'user_country': user_country,
        }

    def login_and_retrieve_profile(self):
        """
        A function that uses the objects username and password and
        retrieves PakWheels profile information.

        Returns:
            returns a dictionary containing all available information on
            profile.

        """
        login_session = self.login_user_and_get_session()
        if login_session is None:
            print ('Credentials provided are invalid. Please try again')
            return None

        profile_url = self.get_user_profile_url(login_session)
        if profile_url is None:
            print ('Unable to retrieve profile URL')
            return None

        user_profile_data = self.extract_user_profile_data(login_session, profile_url)
        return user_profile_data
