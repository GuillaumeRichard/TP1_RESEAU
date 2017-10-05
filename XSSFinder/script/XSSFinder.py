#!/usr/bin/python3
# -*- coding: utf-8 -*-

from robobrowser.exceptions import InvalidSubmitError

from script.LinksFinder import LinksFinder
from script.XSSFlaw import XSSFlaw
from robobrowser import RoboBrowser

VULNERABILITY_TESTING_STRING = '"><script>alert("vulnérable");</script>"'
PARSER = "html.parser"
NO_RESULT_FOUND = "Aucun résultat n'a été trouvé."
URL = "URL : "
PARAMETER = "Nom du paramètre : "
TYPE = "Type (POST ou GET): "
NEW_LINE = "\n"
TWO_NEW_LINES = "\n\n"
EMPTY_STRING = ""


class XSSFinder:

    def __init__(self, url):
        self.list_xss = []
        # self.url = url
        self.browser = RoboBrowser(parser=PARSER, history=True)
        self.browser.open(url)
        self.links_finder = LinksFinder(self.browser.url)

    def find(self):
        links = self.links_finder.get_valid_links()
        for link in links:
            self.browser.open(link)
            forms = self.browser.get_forms()
            for form in forms:
                fields = form.fields
                for field in fields:
                    form[field].value = VULNERABILITY_TESTING_STRING
                    self.validate_xss_weakness(form, field)

    def validate_xss_weakness(self, form, field):
        try:
            self.browser.submit_form(form)
            self.add_threat_to_list(field, form.method)
        except InvalidSubmitError:
            pass

    def add_threat_to_list(self, parameter, xss_type):
        threat = XSSFlaw(self.browser.url, parameter, xss_type)
        if threat not in self.list_xss:
            self.list_xss.append(threat)

    def get_xss_flaws(self):
        self.find()
        if len(self.list_xss) == 0:
            return NO_RESULT_FOUND
        else:
            result = EMPTY_STRING
            for xss_threat in self.list_xss:
                result += URL
                result += xss_threat.get_url()
                result += NEW_LINE
                result += PARAMETER
                result += xss_threat.get_parameter()
                result += NEW_LINE
                result += TYPE
                result += xss_threat.get_xss_type()
                result += TWO_NEW_LINES
            return result



