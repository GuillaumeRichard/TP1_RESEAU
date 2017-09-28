from src.UrlChecker import UrlChecker


class Main:

    urlChecker = None

    def __init__(self, args):
        self.urlChecker = UrlChecker(args[1])
        self.urlChecker.search_for_urls()
        self.urlChecker.check_access_to_directories()