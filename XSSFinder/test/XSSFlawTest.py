import unittest

from script.XSSFlaw import XSSFlaw


class XSSFlawTest(unittest.TestCase):
    def test_compare__url_parameter_and_type_match__returns_true(self):
        url = "a"
        parameter = "b"
        method = "c"
        flaw1 = XSSFlaw(url, parameter, method)
        flaw2 = XSSFlaw(url, parameter, method)

        self.assertEqual(flaw1, flaw2)

    def test_compare__url_does_not_match__returns_false(self):
        url1 = "a"
        url2 = "1"
        parameter = "b"
        method = "c"
        flaw1 = XSSFlaw(url1, parameter, method)
        flaw2 = XSSFlaw(url2, parameter, method)

        self.assertNotEqual(flaw1, flaw2)

    def test_compare__parameter_does_not_match__returns_false(self):
        url = "a"
        parameter1 = "b"
        parameter2 = "1"
        method = "c"
        flaw1 = XSSFlaw(url, parameter1, method)
        flaw2 = XSSFlaw(url, parameter2, method)

        self.assertNotEqual(flaw1, flaw2)

    def test_compare__method_does_not_match__returns_false(self):
        url = "a"
        parameter = "b"
        method1 = "c"
        method2 = "1"
        flaw1 = XSSFlaw(url, parameter, method1)
        flaw2 = XSSFlaw(url, parameter, method2)

        self.assertNotEqual(flaw1, flaw2)
