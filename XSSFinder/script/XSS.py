#!/usr/bin/python3
# -*- coding: utf-8 -*-


class XSS:
    def __init__(self, url, parameter, xss_type):
        self.url = url
        self.parameter = parameter
        self.xss_type = xss_type

    def get_url(self):
        return self.url

    def get_parameter(self):
        return self.parameter

    def get_xss_type(self):
        return self.xss_type

    def __eq__(self, other):
        return self.url == other.url and self.parameter == other.parameter and self.xss_type == other.xss_type
