from optparse import OptionParser

from src.BruteForceLogin import BruteForceLogin
from src.DictionaryReader import DictionaryReader
from src.FormNameFinder import FormNameFinder
from src.MessageAdministrator import MessageAdministrator
from src.Timer import Timer
from src.services.BrowserService import BrowserService


class Main:

    def __init__(self):
        print("Bienvenue à BruteForceLogin.py!")

        args_dictionary = self.get_args()
        message_administrator = MessageAdministrator()
        timer = Timer()
        form_name_finder = FormNameFinder()
        dictionary_reader = DictionaryReader(args_dictionary["dict"])
        browser_service = BrowserService(args_dictionary["url"])
        brute_force_login = BruteForceLogin(
            args_dictionary,
            message_administrator,
            timer,
            form_name_finder,
            dictionary_reader,
            browser_service)

        brute_force_login.execute()

    def get_args(self):
        parser = self.get_parser()
        (options, args) = parser.parse_args()
        return self.create_args_dictionary(options)

    def get_parser(self):
        parser = OptionParser()
        parser.add_option("-r", "--url", dest="url")
        parser.add_option("-d", "--dict", dest="dict")
        parser.add_option("-u", "--username", dest="username")
        parser.add_option("-p", "--passname", dest="passname")
        return parser

    def create_args_dictionary(self, options):
        return {
            "url": options.url,
            "dict": options.dict,
            "username": options.username,
            "passname": options.passname
        }


if __name__ == '__main__':
    Main()
