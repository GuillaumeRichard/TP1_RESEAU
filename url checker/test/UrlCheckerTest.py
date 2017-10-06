from __future__ import print_function
import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from src.UrlChecker import UrlChecker
import inspect

class UrlCheckerTest(unittest.TestCase):

    url = "http://testfire.net/"
    urlChecker = UrlChecker

    def setUp(self):
        self.urlChecker = UrlChecker(self.url)
        self.urlChecker.browser.follow_link = MagicMock()

    def test_init_shouldSaveUrl(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.assertEqual(self.url, self.urlChecker.url)

    def test_init_shouldConnectToUrl(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.assertEqual(self.url, self.urlChecker.browser.url)

    def test_prepareUrl_shouldAddSlashToEndOfURL(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        url = "http://testfire.net"
        expected = self.url

        urlChecker = UrlChecker(url)

        self.assertEqual(expected, urlChecker.url)
        self.assertEqual(expected, urlChecker.browser.url)

    def test_prepareUrl_shouldHandleAutomaticRedirects(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        url = "http://testfire.net/bank"
        expected = self.url
        urlChecker = UrlChecker(url)
        urlChecker.browser.open(expected)

        urlChecker.prepare_url()

        self.assertEqual(expected, urlChecker.url)

    def test_searchForUrls_shouldGoBackWhenOnSameUrlTwice(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        link = "<a href='http://testfire.net/bank'></a>"
        links = [link, link]
        self.urlChecker.browser.get_Links = MagicMock(return_value=links)
        self.urlChecker.browser.back = MagicMock()

        self.urlChecker.search_for_urls()

        self.urlChecker.browser.back.assert_called_once()

    def test_searchForUrls_shouldGoBackWhenOutsideOfSourceUrl(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        link = "<a href='http://testfire.net/bank'></a>"
        badlink = "<a href='https://www.youtube.com/'></a>"
        links = [link, badlink]
        self.urlChecker.browser.get_links = MagicMock(return_value=links)
        self.urlChecker.visitedURLs = []
        self.urlChecker.browser.back = MagicMock()

        self.urlChecker.search_for_urls()

        self.urlChecker.browser.back.assert_called_once()

    def test_checkAccessToDirectories_shouldNotCheckIfThereAreNoDirectories(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.urlChecker.check_directory = MagicMock()
        self.urlChecker.visitedURLs = [self.url]

        self.urlChecker.check_access_to_directories()

        self.urlChecker.check_directory.assert_not_called()

    def test_checkAccessToDirectories_shouldCheckIfThereAreDirectories(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.urlChecker.check_directory = MagicMock()
        self.urlChecker.visitedURLs = [self.url, self.url + "/bank"]

        self.urlChecker.check_access_to_directories()

        self.urlChecker.check_directory.assert_called_once()

    def test_checkAccessToDirectories_shouldSayIfThereIsASecurityBreach(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.urlChecker.check_directory = MagicMock()
        self.urlChecker.suspiciousDirectories = ["ok"]
        self.urlChecker.print_function = MagicMock()

        self.urlChecker.check_access_to_directories()

        self.urlChecker.print_function\
            .assert_called_with("The website is suspected to have lacking directory protection!")

    def test_checkAccessToDirectories_shouldSayIfThereIsNoSecurityBreach(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.urlChecker.check_directory = MagicMock()
        self.urlChecker.suspiciousDirectories = []
        self.urlChecker.print_function = MagicMock()

        self.urlChecker.check_access_to_directories()

        self.urlChecker.print_function\
            .assert_called_with("The website had no suspicious activities about directory access.")

    def test_checkDirectory_shouldNotCheckSameDirectoryTwice(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.urlChecker.checkedDirectories = [self.url]
        self.urlChecker.browser.open = MagicMock()

        self.urlChecker.check_directory(self.url)

        self.urlChecker.browser.open.assert_not_called()

    def test_checkDirectory_shouldNotSuspectNormalDirectories(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.urlChecker.browser = Mock(parsed=Mock(text='okok'))
        self.urlChecker.browser.open = MagicMock()

        self.urlChecker.check_directory(self.url)

        self.assertEqual(0, len(self.urlChecker.suspiciousDirectories))

    def test_checkDirectory_shouldSuspectDirectoriesWithToParentDirectory(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        suspiciousUrl = "suspicious url"
        self.urlChecker.browser = Mock(parsed=Mock(text='To Parent Directory'))
        self.urlChecker.browser.open = MagicMock()

        self.urlChecker.check_directory(suspiciousUrl)

        self.assertEqual(self.urlChecker.suspiciousDirectories[0], suspiciousUrl)

    def test_checkDirectory_shouldSuspectDirectoriesWithIndex(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        suspiciousUrl = "suspicious url"
        self.urlChecker.browser = Mock(parsed=Mock(text='Index'))
        self.urlChecker.browser.open = MagicMock()

        self.urlChecker.check_directory(suspiciousUrl)

        self.assertEqual(self.urlChecker.suspiciousDirectories[0], suspiciousUrl)

    def test_checkDirectory_shouldWarnIfDirectoryIsSuspicious(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        suspiciousUrl = "bad url"
        self.urlChecker.print_function = MagicMock()
        self.urlChecker.browser = Mock(parsed=Mock(text='Index'))
        self.urlChecker.browser.open = MagicMock()

        self.urlChecker.check_directory(suspiciousUrl)

        self.urlChecker.print_function.assert_called_once_with(suspiciousUrl + " is suspicious!")

    def test_startUp_shouldAlertConnection(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.urlChecker.print_function = MagicMock()
        self.urlChecker.browser.open = MagicMock()

        self.urlChecker.start_up(self.url)

        self.urlChecker.print_function.assert_called_once_with("Connecting to " + str(self.url) + " ...")

    def test_startUp_shouldAlertConnectionFailed(self):
        frame = inspect.currentframe()
        print(inspect.getframeinfo(frame).function)

        self.urlChecker.print_function = MagicMock()

        self.urlChecker.start_up("http://badurl.com")

        self.urlChecker.print_function.assert_any_call("Connexion failed.")


if __name__ == '__main__':
    unittest.main()