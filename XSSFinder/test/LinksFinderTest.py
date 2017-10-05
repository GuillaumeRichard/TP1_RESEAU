#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

from robobrowser import RoboBrowser
from robobrowser.exceptions import RoboError

from script.LinksFinder import LinksFinder
from unittest.mock import MagicMock, PropertyMock

ANY_NOT_SECURED_URL = "http://www.test.com/"
PARSER = "html.parser"


class LinksFinderTest(unittest.TestCase):
    def test_get_url_base__returns_url_base(self):
        long_url = "http://www.potato.com/content=pepe/rare.htm"
        expected_url = "http://www.potato.com/"
        links_finder = LinksFinder(expected_url)

        actual_url = links_finder.get_url_base(long_url)

        self.assertEqual(expected_url, actual_url)

    def test_are_url_similar__when_url_are_similar__returns_true(self):
        long_url = "http://www.potato.com/content=pepe/rare.htm"
        short_url = "http://www.potato.com/"
        links_finder = LinksFinder(long_url)
        links_finder.url = short_url

        self.assertTrue(links_finder.are_url_similar(long_url))

    def test_are_url_similar__when_url_are_not_similar__returns_false(self):
        long_url = "http://www.pomodoro.com/content=pepe/rare.htm"
        short_url = "http://www.potato.com/"
        links_finder = LinksFinder(long_url)
        links_finder.url = short_url

        self.assertFalse(links_finder.are_url_similar(long_url))

    def test_get_valid_links__returns_list_of_url(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        expected_url_list = links_finder.url_list
        links_finder.add_valid_links = MagicMock()

        actual_url_list = links_finder.get_valid_links()

        self.assertEqual(expected_url_list, actual_url_list)

    def test_add_valid_link__when_the_link_is_invalid__then_the_link_is_not_in_list(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        link = MagicMock()
        browser = RoboBrowser(parser=PARSER, history=True)
        browser.follow_link = MagicMock(side_effect=RoboError)

        links_finder.add_valid_link(browser, link)
        actual_url_list = links_finder.url_list

        self.assertTrue(link not in actual_url_list)

    def test_add_valid_link__when_the_link_is_another_web_site__then_the_link_is_not_in_list(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        link = MagicMock()
        browser = MagicMock()
        browser.follow_link = MagicMock()
        links_finder.are_url_similar = MagicMock(return_value=False)

        links_finder.add_valid_link(browser, link)
        actual_url_list = links_finder.url_list

        self.assertTrue(link not in actual_url_list)

    def test_add_valid_link__when_the_url_is_already_in_the_list__then_the_url_is_not_added_twice_in_the_list(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        link = MagicMock()
        link_url = ANY_NOT_SECURED_URL + "login"
        links_finder.url_list.append(link_url)
        browser = MagicMock()
        browser.url = PropertyMock(link_url)
        browser.follow_link = MagicMock()
        links_finder.are_url_similar = MagicMock(return_value=True)
        links_finder.does_page_contains_form = MagicMock(return_value=True)

        links_finder.add_valid_link(browser, link)

        self.assertTrue(links_finder.url_list.count(link_url) == 1)

    def test_add_valid_link__when_the_link_page_has_no_form__then_the_link_is_not_in_list(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        link = MagicMock()
        link_url = ANY_NOT_SECURED_URL + "login"
        browser = MagicMock()
        browser.url = PropertyMock(link_url)
        browser.follow_link = MagicMock()
        links_finder.are_url_similar = MagicMock(return_value=True)
        links_finder.does_page_contains_form = MagicMock(return_value=False)

        links_finder.add_valid_link(browser, link)
        actual_url_list = links_finder.url_list

        self.assertTrue(link not in actual_url_list)

    def test_add_valid_link__when_the_valid_url_is_not_in_the_list__then_the_url_added_in_the_list(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        link_url = ANY_NOT_SECURED_URL + "login"
        link = MagicMock()
        browser = MagicMock()
        browser.follow_link = MagicMock()
        browser.url = PropertyMock(link_url)
        links_finder.are_url_similar = MagicMock(return_value=True)
        links_finder.does_page_contains_form = MagicMock(return_value=True)

        links_finder.add_valid_link(browser, link)

        self.assertTrue(browser.url in links_finder.url_list)

    def test_add_valid_link__when_link_is_valid__then_the_browser_is_on_the_same_url(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        link = MagicMock()
        browser = MagicMock()
        url_before = browser.url
        browser.follow_link = MagicMock()
        links_finder.are_url_similar = MagicMock(return_value=True)
        links_finder.does_page_contains_form = MagicMock(return_value=True)

        links_finder.add_valid_link(browser, link)
        url_after = browser.url

        self.assertTrue(url_before == url_after)

    def test_add_valid_link__when_link_is_invalid__then_the_browser_is_on_the_same_url(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        link = MagicMock()
        browser = MagicMock()
        url_before = browser.url
        browser.follow_link = MagicMock(side_effect=RoboError)

        links_finder.add_valid_link(browser, link)
        url_after = browser.url

        self.assertTrue(url_before == url_after)

    def test_add_valid_link__when_url_are_not_similar__then_the_browser_is_on_the_same_url(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        link = MagicMock()
        browser = MagicMock()
        url_before = browser.url
        browser.follow_link = MagicMock()
        links_finder.are_url_similar = MagicMock(return_value=False)

        links_finder.add_valid_link(browser, link)
        url_after = browser.url

        self.assertTrue(url_before == url_after)

    def test_add_valid_link__when_url_is_in_the_list__then_the_browser_is_on_the_same_url(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        link = MagicMock()
        link_url = ANY_NOT_SECURED_URL + "login"
        links_finder.url_list.append(link_url)
        browser = MagicMock()
        url_before = browser.url
        browser.follow_link = MagicMock()
        links_finder.are_url_similar = MagicMock(return_value=True)
        links_finder.does_page_contains_form = MagicMock(return_value=True)

        links_finder.add_valid_link(browser, link)
        url_after = browser.url

        self.assertTrue(url_before == url_after)

    def test_does_page_contains_form__page_has_at_least_a_form__returns_true(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        browser = MagicMock()
        browser.get_forms = MagicMock(return_value=["form"])

        self.assertTrue(links_finder.does_page_contains_form(browser))

    def test_does_page_contains_form__page_has_no_form__returns_false(self):
        links_finder = LinksFinder(ANY_NOT_SECURED_URL)
        browser = MagicMock()
        browser.get_forms = MagicMock(return_value=[])

        self.assertFalse(links_finder.does_page_contains_form(browser))
