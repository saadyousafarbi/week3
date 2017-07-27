import requests

from bs4 import BeautifulSoup

from ZameenProfile import ZameenProfile
from BaseScraper import BaseScraper


class ZameenScraper(BaseScraper):

    def __init__(self, base_url, username, password):
        """
        Extends base class BaseScraper.

        Attributes:
            base_url (str) : Base URL provided by user of website
            username (str) : Username credential of user
            password (str) : Password credential of user
            self.login_url (str): Zameen's URL for logging in derived from base URL
            self.profile_url (str) : Zameen's static url containing profile

        """
        BaseScraper.__init__(self, base_url, username, password)
        self.login_url = '{0}/login.html'.format(base_url)
        self.profile_url = 'http://profolio.zameen.com/profolio/'

    def login_and_retrieve_profile(self):
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
        headers_data = {
            'Referer': 'https://www.zameen.com/login.html',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/55.0.2883.87 Safari/537.36',
        }
        login_data = {
            'email': self.username,
            'password': self.password,
            'keep' : 'keep',
            'submit': 1,
            'action_login': 1,
        }
        print self.login_url
        response = session.post(self.login_url, data=login_data, headers=headers_data)
        if 'Logged in' in response.text:
            print 'Login successful for the user: {}'.format(self.username)
            print 'Zameen profile as follows'
            soup = BeautifulSoup(response.content, 'html.parser')
            profile_link = soup.findAll('a', href=True, text='My Account & Profiles')
            profile_link = profile_link[0]['href']
            profile_info = session.get(self.profile_url +
                                       profile_link,
                                       headers=headers_data
                                       ).text
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
            zameen_profile = ZameenProfile(user_name,
                                       user_email,
                                       user_phone_number,
                                       user_address,
                                       user_country,
                                       )
            zameen_profile.print_user_profile()
            return zameen_profile
        else:
            print ('Credentials provided are invalid. Please try again')
