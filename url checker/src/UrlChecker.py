from robobrowser import RoboBrowser


class UrlChecker:

    def start_up(self):
        browser = RoboBrowser(history=True)
        browser.open("http://localhost:8080")

        toolbar = browser.select("a");
        browser.follow_link(toolbar[3])

    def __init__(self):
        self.start_up()

