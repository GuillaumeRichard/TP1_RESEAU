import sys

from src.MessageAdministrator import MessageAdministrator
from src.services.BeautifulSoupService import BeautifulSoupService
from src.exceptions.FormNotFoundError import FormNotFoundError

class FormNameFinder:

    def __init__(self):
        self.beautiful_soup_service = BeautifulSoupService()

    def get_form_name(self, url, username, passname):
        forms = self.beautiful_soup_service.get_form_list(url)

        for form in forms:
            str_form = form.prettify()  # convertir le formulaire en string
            if username in str_form and passname in str_form:
                str_after_name = str_form.split("id=\"", 1)[1]  # ex: <form id="uid" name="id">...
                                                                # devient
                                                                #  uid" id="id">

                return str_after_name.split("\"", 1)[0]         # ex: uid" name="id">
                                                                # devient
                                                                # uid

        error_message = MessageAdministrator.get_form_not_found_message(username, passname)
        raise FormNotFoundError(error_message)

