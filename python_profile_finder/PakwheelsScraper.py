import requests
import datetime

from bs4 import BeautifulSoup

from BaseScraper import BaseScraper


class PakwheelsScraper(BaseScraper):
    base_url = 'https://www.pakwheels.com'

    def __init__(self, username, password):
        """
        Extends base class BaseScraper
        """
        self.username = username
        self.password = password
        self.login_url = self.get_login_url()
        self.post_url = self.get_login_post_url()

    def get_login_url(self):
        """
        Method constructs login url.
        """
        login_url = '{base_url}/login'.format(base_url=self.base_url)
        return login_url

    @classmethod
    def get_login_post_url(self):
        """
        Method constructs post url for login form.
        """
        login_post_url = '{base_url}/sessions'.format(base_url=self.base_url)
        return login_post_url

    def get_user_profile_url(self, login_session):
        """
        Retrieve profile url for logged in user.

        Arguments:
            login_session (session): A session with user logged in

        Returns:
            profile_url (str): A url string of the users profile

        """
        response = login_session.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        extracted_profile_links = soup.findAll('a', href=True, text='Profile')
        profile_url = None
        if extracted_profile_links:
            profile_url = '{base_url}/{extracted_profile_link}'.format(
               base_url=self.base_url, extracted_profile_link =extracted_profile_links[0]['href']
            )

        return profile_url

    def login_user_and_get_session(self):
        """
        Login user and return request session.

        returns:
            session (session): Returns a logged in session
        """
        session = requests.Session()
        print self.login_url
        html = session.get(self.login_url).text
        soup = BeautifulSoup(html, 'html.parser')
        utf_field = soup.find_all('input', type='hidden')[0].get('value')
        authentication_token = soup.find_all('input', type='hidden')[1].get('value')

        headers_data = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.pakwheels.com',
        }
        login_data = {
            'username': self.username,
            'password': self.password,
            'authenticity_token': authentication_token,
            'utf8': utf_field,
            'code': '',
            'provider': '',
        }
        print self.post_url
        response = session.post(self.post_url, data=login_data, headers=headers_data)
        if 'Sign-In Successful' in response.content:
            print 'Login successful for the user: {}'.format(self.username)
            return session

        return None

    def extract_user_profile_data(self, login_session, profile_url):
        """
        Returns a Pakwheels user profile information.

        Arguments:
            login_session (session): logged in session of the user
            profile_url (str): url of the users profile

        Returns:
            Returns a dictionary object containing profile info of user

        """
        profile_info = login_session.get(profile_url).text
        soup = BeautifulSoup(profile_info, 'html.parser')
        user_name = soup.find('input', {'id': 'user_username'}).get('value')
        name = soup.find('input', {'id': 'user_display_name'}).get('value')
        spliced_name = name.split()
        first_name = spliced_name[0]
        last_name = spliced_name[1]
        user_gender = soup \
            .find('select', {'id': 'user_gender'}) \
            .find('option', selected=True) \
            .get('value')

        user_birthday = soup.find('input', {'id': 'user_birthday'}).get('value')
        formatted_user_birthday = datetime.datetime.strptime(user_birthday, "%d-%m-%Y").strftime("%Y-%m-%d")
        user_city = soup \
            .find('select', {'id': 'user_city'}) \
            .find('option', selected=True) \
            .get('value')

        user_country = soup \
            .find('select', {'id': 'user_country'}) \
            .find('option', selected=True) \
            .get('value')

        user_email = soup.find('input', {'id': 'user_email'}).get('value')
        return {
            'first_name': first_name,
            'last_name': last_name,
            'user_name': user_name,
            'user_gender': user_gender,
            'user_email': user_email,
            'user_birthday': formatted_user_birthday,
            'user_city': user_city,
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
