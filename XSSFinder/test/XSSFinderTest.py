#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import pytest
import unittest

from robobrowser.exceptions import InvalidSubmitError
from script.XSS import XSS
from script.XSSFinder import XSSFinder
from unittest.mock import MagicMock


class XSSFinderTest(unittest.TestCase):
    def test_validate_xss_weakness__form_cannot_be_submit__catches_exception(self):
        url = "http://test.com/"
        xss_finder = XSSFinder(url)
        form = "Search"
        field = MagicMock()
        xss_finder.browser.submit_form = MagicMock(side_effect=InvalidSubmitError)
        expected_number_of_threats = len(xss_finder.list_xss)

        xss_finder.validate_xss_weakness(form, field)

        self.assertTrue(expected_number_of_threats == len(xss_finder.list_xss))

    def test_validate_xss_weakness__form_is_submit__add_threat_to_list(self):
        url = "http://test.com/"
        xss_finder = XSSFinder(url)
        expected_number_of_threats = len(xss_finder.list_xss) + 1
        xss_finder.browser.submit_form = MagicMock()
        form = MagicMock()
        field = MagicMock()

        xss_finder.validate_xss_weakness(form, field)

        self.assertTrue(expected_number_of_threats == len(xss_finder.list_xss))

    def test_add_threat_to_list__threat_is_added_to_list(self):
        url = "http://test.com/"
        xss_parameter = "Search"
        xss_method = "GET"
        expected_xss_flaw = XSS(url, xss_parameter, xss_method)
        xss_finder = XSSFinder(url)

        xss_finder.add_threat_to_list(xss_parameter, xss_method)

        self.assertTrue(expected_xss_flaw in xss_finder.list_xss)

    def test_get_xss_flaws__no_flaw_founded__returns_no_result_founded(self):
        no_result_founded = "Aucun résultat n'a été trouvé."
        url = ""
        xss_finder = XSSFinder(url)
        xss_finder.find = MagicMock()

        self.assertTrue(no_result_founded == xss_finder.get_xss_flaws())

    def test_get_xss_flaws__flaws_founded__returns_flaws(self):
        url = "http://test.com/"
        search_xss_parameter = "Search"
        search_method = "GET"
        sign_in_xss_parameter = "SignIn"
        sign_in_method = "POST"
        RESULT_FOUND = "URL : " + url + "\nNom du paramètre : " + search_xss_parameter + \
                       "\nType (POST ou GET): " + search_method + "\n\n" + \
                       "URL : " + url + "\nNom du paramètre : " + sign_in_xss_parameter + \
                       "\nType (POST ou GET): " + sign_in_method + "\n\n"
        search_xss = XSS(url, search_xss_parameter, search_method)
        sign_in_xss = XSS(url, sign_in_xss_parameter, sign_in_method)
        xss_finder = XSSFinder(url)
        xss_finder.list_xss.append(search_xss)
        xss_finder.list_xss.append(sign_in_xss)
        xss_finder.find = MagicMock()

        self.assertTrue(RESULT_FOUND == xss_finder.get_xss_flaws())
