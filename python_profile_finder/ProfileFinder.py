import optparse

from ZameenScraper import ZameenScraper
from PakwheelsScraper import PakwheelsScraper

parser = optparse.OptionParser()
parser.add_option('-w', '--website', dest='website', help='Enter your website starting with https://')
parser.add_option('-c', '--credential', dest='entry_credential', help='Your Entry Info')
parser.add_option('-p', '--password', dest='password', help='Your Password')

(options, args) = parser.parse_args()

if options.website is None:
    options.website = raw_input('Enter Website:')

if options.entry_credential is None:
    options.entry_credential = raw_input('Enter Entry Credentials:')

if options.password is None:
    options.password = raw_input('Enter Password:')

if 'zameen' in options.website:
    get_zameen_profile = ZameenScraper(options.website,
                                       options.entry_credential,
                                       options.password)
    get_zameen_profile.login_and_retrieve_profile()

elif 'pakwheels' in options.website:
    get_pakwheels_profile = PakwheelsScraper(options.website,
                                             options.entry_credential,
                                             options.password)
    get_pakwheels_profile.login_and_retieve_profile()

