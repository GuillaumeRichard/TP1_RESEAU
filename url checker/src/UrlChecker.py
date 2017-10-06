from robobrowser import RoboBrowser
from httplib2 import Http
import requests

class UrlChecker:

    url = ""
    browser = None
    siteAllowsDirectoryList = False
    checkedDirectories = []
    suspiciousDirectories = []
    visitedURLs = []
    http = Http()

    def print_function(self,text):
        print(text)

    def search_for_urls(self):
        links = self.browser.get_links()
        for link in links:
            if self.browser.url in self.visitedURLs:
                break
            elif self.url not in self.browser.url:
                self.browser.back()
                break
            else:
                try:
                    self.browser.follow_link(link)
                    self.print_function('Navigating '+self.browser.url+' ...')
                    self.visitedURLs.append(self.browser.url)
                    self.search_for_urls()
                    self.browser.back()
                except:
                    self.print_function('Error in link, ignored.')
                    pass

    def prepare_url(self):
        if self.url != self.browser.url:
            self.url = self.browser.url
        if not self.url.endswith("/"):
            self.url += "/"

    def check_directory(self, url):
        if url not in self.checkedDirectories:
            self.checkedDirectories.append(url)
            self.browser.open(url)
            content = self.browser.parsed
            if 'To Parent Directory' in content.text or 'Index' in content.text:
                self.print_function(url + " is suspicious!")
                self.suspiciousDirectories.append(url)

    def check_access_to_directories(self):
        self.print_function("Checking access to directories...")
        for url in self.visitedURLs:
            url = url.replace(self.url, "")
            directories = url.split("/")
            if len(directories) > 1 :
                for x in range(0, len(directories) - 1):
                    url = self.url + directories[x] + "/"
                    self.check_directory(url)
        if len(self.suspiciousDirectories) > 0:
            self.print_function("The website is suspected to have lacking directory protection!")
        else :
            self.print_function("The website had no suspicious activities about directory access.")

    def validate_url(self, url):
        request = requests.get(url)
        if request.status_code != 200:
            raise ConnectionError

    def start_up(self, url):
        self.print_function('Connecting to '+str(url)+' ...')
        try:
            self.validate_url(url)
            self.browser = RoboBrowser(history=True, parser='html.parser')
            self.browser.open(str(url))
            self.prepare_url()
        except requests.exceptions.ConnectionError :
            self.print_function("Connexion failed.")

    def __init__(self, url):
        self.start_up(url)

