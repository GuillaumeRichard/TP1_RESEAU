#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import pytest
import unittest

from robobrowser.exceptions import InvalidSubmitError
from script.XSSFlaw import XSSFlaw
from script.XSSFinder import XSSFinder
from unittest.mock import MagicMock

ANY_NOT_SECURED_URL = "http://test.com/"


class XSSFinderTest(unittest.TestCase):
    def test_validate_xss_weakness__form_cannot_be_submit__catches_exception(self):
        xss_finder = XSSFinder(ANY_NOT_SECURED_URL)
        form = "Search"
        field = MagicMock()
        xss_finder.browser.submit_form = MagicMock(side_effect=InvalidSubmitError)
        expected_number_of_threats = len(xss_finder.list_xss)

        xss_finder.validate_xss_weakness(form, field)

        self.assertTrue(expected_number_of_threats == len(xss_finder.list_xss))

    def test_validate_xss_weakness__form_is_submit__add_threat_to_list(self):
        xss_finder = XSSFinder(ANY_NOT_SECURED_URL)
        expected_number_of_threats = len(xss_finder.list_xss) + 1
        xss_finder.browser.submit_form = MagicMock()
        form = MagicMock()
        field = MagicMock()

        xss_finder.validate_xss_weakness(form, field)

        self.assertTrue(expected_number_of_threats == len(xss_finder.list_xss))

    def test_add_threat_to_list__threat_is_added_to_list(self):
        xss_parameter = "Search"
        xss_method = "GET"
        expected_xss_flaw = XSSFlaw(ANY_NOT_SECURED_URL, xss_parameter, xss_method)
        xss_finder = XSSFinder(ANY_NOT_SECURED_URL)

        xss_finder.add_threat_to_list(xss_parameter, xss_method)

        self.assertTrue(expected_xss_flaw in xss_finder.list_xss)

    def test_get_xss_flaws__no_flaw_founded__returns_no_result_founded(self):
        no_result_founded = "Aucun résultat n'a été trouvé."
        xss_finder = XSSFinder(ANY_NOT_SECURED_URL)
        xss_finder.find = MagicMock()

        self.assertTrue(no_result_founded == xss_finder.get_xss_flaws())

    def test_get_xss_flaws__flaws_founded__returns_flaws(self):
        search_xss_parameter = "Search"
        search_method = "GET"
        sign_in_xss_parameter = "SignIn"
        sign_in_method = "POST"
        RESULT_FOUND = "URL : " + ANY_NOT_SECURED_URL + "\nNom du paramètre : " + search_xss_parameter + \
                       "\nType (POST ou GET): " + search_method + "\n\n" + \
                       "URL : " + ANY_NOT_SECURED_URL + "\nNom du paramètre : " + sign_in_xss_parameter + \
                       "\nType (POST ou GET): " + sign_in_method + "\n\n"
        search_xss = XSSFlaw(ANY_NOT_SECURED_URL, search_xss_parameter, search_method)
        sign_in_xss = XSSFlaw(ANY_NOT_SECURED_URL, sign_in_xss_parameter, sign_in_method)
        xss_finder = XSSFinder(ANY_NOT_SECURED_URL)
        xss_finder.list_xss.append(search_xss)
        xss_finder.list_xss.append(sign_in_xss)
        xss_finder.find = MagicMock()

        self.assertTrue(RESULT_FOUND == xss_finder.get_xss_flaws())
