import optparse
import getpass

from PakwheelsProfile import PakwheelsProfile
from PakwheelsScraper import PakwheelsScraper
from ZameenScraper import ZameenScraper
from ZameenProfile import ZameenProfile


SUPPORTED_WEBSITES = ['pakwheels', 'zameen']


parser = optparse.OptionParser()
parser.add_option(
    '-w',
    '--website',
    dest='website',
    help='Enter website name from {supported_websites}'.format(supported_websites=SUPPORTED_WEBSITES)
)
parser.add_option('-c', '--credential', dest='login_credential', help='Your login username/email')
parser.add_option('-p', '--password', dest='login_password', help='Your login password')

(options, args) = parser.parse_args()

while True:
    if options.website not in SUPPORTED_WEBSITES:
        options.website = raw_input(
            'Enter website name from {supported_websites} again: '.format(supported_websites=SUPPORTED_WEBSITES)
        )
    else:
        break

if options.login_credential is None:
    options.login_credential = raw_input('Your login username/email: ')

if options.login_password is None:
    options.login_password = getpass.getpass('Your login password: ')

if 'pakwheels' in options.website:
    pakwheels_scraper = PakwheelsScraper(
        options.login_credential,
        options.login_password,
    )
    profile_data = pakwheels_scraper.login_and_retrieve_profile()
    pakwheels_profile = PakwheelsProfile(
        name=profile_data['user_name'],
        email=profile_data['user_email'],
        birthday=profile_data['user_birthday'],
        city=profile_data['user_city'],
        country=profile_data['user_country'],
    )
    pakwheels_profile.print_user_profile()

if 'zameen' in options.website:
    zameen_scraper = ZameenScraper(
        options.login_credential,
        options.login_password,
    )
    profile_data = zameen_scraper.login_and_retrieve_profile()
    zameen_profile = ZameenProfile(
        name=profile_data['user_name'],
        email=profile_data['user_email'],
        phone_number=profile_data['user_phone_number'],
        address=profile_data['user_address'],
        country=profile_data['user_country'],
    )
    zameen_profile.print_user_profile()
