#!/usr/bin/python3
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser
from robobrowser.exceptions import RoboError

PARSER = "html.parser"
STARTING_URL = "http://"
TWO_DOTS = "../"
EMPTY = ""
SLASH = "/"
THIRD_SLASH = 3
VALID_CODE = 200


class LinksFinder:

    def __init__(self, url):
        self.url = url
        self.url_list = [self.url]

    def are_url_similar(self, url):
        url_base = self.get_url_base(url)
        main_url_base = self.get_url_base(self.url)
        return url_base == main_url_base

    def get_url_base(self, url):
        split_slash = url.split(SLASH)[:THIRD_SLASH]
        base = EMPTY
        for seg in split_slash:
            base += seg + SLASH
        return base

    def get_valid_links(self):
        for url in self.url_list:
            self.add_valid_links(url)
        return self.url_list

    def add_valid_links(self, url):
        browser = RoboBrowser(parser=PARSER, history=True)
        browser.open(url)
        links = browser.get_links()
        for link in links:
            self.add_valid_link(browser, link)

    def add_valid_link(self, browser, link):
        try:
            browser.follow_link(link)
            if self.are_url_similar(browser.url):
                if self.does_page_contains_form(browser):
                    if browser.url not in self.url_list:
                        self.url_list.append(browser.url)
            browser.back()
        except RoboError:
            pass

    def does_page_contains_form(self, browser):
        return len(browser.get_forms()) is not 0


