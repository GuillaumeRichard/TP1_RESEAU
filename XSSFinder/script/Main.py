#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from script.XSSFinder import XSSFinder

MISSING_ARGUMENT_MESSAGE = "Il manque un argument pour le url."


class Main:

    @staticmethod
    def execute(arguments):
        if len(arguments) < 2:
            return MISSING_ARGUMENT_MESSAGE
        finder = XSSFinder(arguments[1])
        return finder.get_xss_flaws()


if __name__ == '__main__':
    answer = Main.execute(sys.argv)
    print(answer)
