import requests

from bs4 import BeautifulSoup

from PakwheelsProfile import PakwheelsProfile
from BaseScraper import BaseScraper


class PakwheelsScraper(BaseScraper):

    def __init__(self, base_url, username, password):
        """
        Extends base class BaseScraper

        """
        BaseScraper.__init__(self, base_url, username, password)
        self.login_url = '{0}/login'.format(base_url)
        self.post_url = '{0}/sessions'.format(base_url)

    def login_and_retrieve_profile(self):
        """
        A function that uses the objects username and password and
        retrieves PakWheels profile information.

        Arguments:
            self

        :return:
            returns an object containing all available information on
            profile and also prints information

        """
        session = requests.Session()
        print self.login_url
        html = session.get(self.login_url).text
        soup = BeautifulSoup(html, 'html.parser')
#        utf_field = soup.find_all('input', type='hidden')[0].get('value')
        authentication_token = soup.find_all('input', type='hidden')[1].get('value')

        headers_data = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.pakwheels.com',
        }
        login_data = {
            'username': self.username,
            'password': self.password,
            'authenticity_token': authentication_token,
            # 'utf8': utf_field,
            # 'code': '',
            # 'provider': '',
        }
        print self.post_url
        response = session.post(self.post_url, data=login_data)
        if 'Sign-In Successful' in response.content:
            print 'Login successful for the user: {}'.format(self.username)
            print 'PakWheels profile as follows'
            soup = BeautifulSoup(response.content, 'html.parser')
            profile_link = soup.findAll('a', href=True, text='Profile')

            if profile_link:
                profile_info = session.get('https://www.pakwheels.com/'+profile_link[0]['href']).text
                soup = BeautifulSoup(profile_info, 'html.parser')
                user_name = soup.find('input', {'id': 'user_display_name'}).get('value')
                user_birthday = soup.find('input', {'id': 'user_birthday'}).get('value')
                user_city = soup \
                    .find('select', {'id': 'user_city'}) \
                    .find('option', selected=True) \
                    .get('value')

                user_country = soup \
                    .find('select', {'id': 'user_country'}) \
                    .find('option', selected=True) \
                    .get('value')

                user_email = soup.find('input', {'id': 'user_email'}).get('value')

                user_profile = PakwheelsProfile(user_name,
                                        user_email,
                                        user_birthday,
                                        user_city,
                                        user_country,
                                            )
                user_profile.print_user_profile()
                return user_profile

        else:
            print ('Credentials provided are invalid. Please try again')
