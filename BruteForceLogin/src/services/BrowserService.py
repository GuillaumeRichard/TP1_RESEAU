import requests
from robobrowser import RoboBrowser

from src.exceptions.BadUrlError import BadUrlError
from src.MessageAdministrator import MessageAdministrator


class BrowserService:

    form = None

    def __init__(self, url):
        self.browser = RoboBrowser(parser='html.parser')
        self.base_url = url

        self.validate_url(url)

        self.browser.open(self.base_url)

    def validate_url(self, url):
        request = requests.get(url)
        if request.status_code != 200:
            message = MessageAdministrator.get_url_not_found_message(url)
            raise BadUrlError(message)

    def set_form(self, form_name):
        self.form = self.browser.get_form(form_name)

    def fill_form(self, user_field, password_field, password, username_to_enter):
        self.form[user_field].value = username_to_enter
        self.form[password_field].value = password
        self.form.serialize()

        self.browser.submit_form(self.form)

    def verify_url_has_changed(self):
        return self.base_url != self.browser.url

