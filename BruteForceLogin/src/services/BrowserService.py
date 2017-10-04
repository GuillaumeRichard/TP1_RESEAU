from robobrowser import RoboBrowser


class BrowserService:

    def __init__(self, url):
        self.browser = RoboBrowser(parser='html.parser')
        self.base_url = url

        self.browser.open(self.base_url)

    def get_form(self, form_name):
        return self.browser.get_form(form_name)

    def submit_form(self, form):
        self.browser.submit_form(form)

    def verify_url_has_changed(self):
        return self.base_url != self.browser.url
