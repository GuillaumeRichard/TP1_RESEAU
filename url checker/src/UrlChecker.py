from robobrowser import RoboBrowser
from httplib2 import Http

class UrlChecker:

    url = ""
    browser = None
    siteAllowsDirectoryList = False
    checkedDirectories = []
    visitedURLs = []

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
                    print('Navigating ', self.browser.url, ' ...')
                    self.visitedURLs.append(self.browser.url)
                    self.search_for_urls()
                    self.browser.back()
                except:
                    print('Error in link, ignored.')
                    pass

    def prepare_url(self):
        if not self.url.endswith("/"):
            self.url += "/"

    def check_directory(self, url):
        if url not in self.checkedDirectories:
            http = Http('.cache')
            self.checkedDirectories.append(url)
            response, content = http.request(url)
            if b'To Parent Directory' in content:
                print(url + " is suspicious!")

    def check_access_to_directories(self):
        self.prepare_url()
        print("Checking access to directories...")
        for url in self.visitedURLs:
            url = url.replace(self.url, "")
            directories = url.split("/")
            if len(directories) > 1 :
                for x in range(0, len(directories) - 1):
                    url = self.url + directories[x] + "/"
                    self.check_directory(url)



    def start_up(self, url):
        print('Connecting to ', str(url), ' ...')
        try:
            self.browser = RoboBrowser(history=True, parser='html.parser')
            self.browser.open(str(url))
        except:
            print("Connexion failed.")
            exit()

    def __init__(self, url):
        self.start_up(url)
        self.url = url

