from optparse import OptionParser
from BruteForceLogin import BruteForceLogin


class Main:

    def __init__(self):
        print("Bienvenue à BruteForceLogin.py!")

        args_dictionary = self.get_args()
        BruteForceLogin(args_dictionary)

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
