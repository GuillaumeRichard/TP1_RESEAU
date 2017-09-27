from robobrowser import RoboBrowser


class UrlChecker:

    url = ""
    browser = None
    siteAllowsDirectoryList = False
    foundDirectories = []
    visitedDirectories = []

    def searchForDirectories(self):
        links = self.browser.get_links()
        for link in links:
            if self.browser.url in self.visitedDirectories:
                break
            elif self.url not in self.browser.url:
                self.browser.back()
                break
            else:
                try:
                    self.browser.follow_link(link)
                    print('Navigating ', self.browser.url, ' ...')
                    self.visitedDirectories.append(self.browser.url)
                    self.searchForDirectories()
                    self.browser.back()
                except:
                    print('Error in link, ignored.')
                    pass

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

