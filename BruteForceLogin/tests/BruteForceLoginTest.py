import unittest
from unittest.mock import Mock

from src.BruteForceLogin import BruteForceLogin
from tests.MockPrintAnswer import MockPrintAnswer
from src.MessageAdministrator import MessageAdministrator


class BruteForceLoginTest(unittest.TestCase):

    USERNAME = "admin"
    PASSWORD = "royalcanin"
    MINUTES = "15"

    def setUp(self):
        self.args_dictionary = self.create_args_dictionary()
        self.create_mocks()
        self.create_brute_force_login()
        self.brute_force_login.input_function = self.input_value
        self.set_return_values()

    def create_args_dictionary(self):
        return {
            "url": "url",
            "dict": "dict",
            "username": "username",
            "passname": "passname"
        }

    def create_mocks(self):
        self.mock_print = MockPrintAnswer()
        self.message_administrator = MessageAdministrator()
        self.message_administrator.print_function = self.mock_print.print_answer
        self.timer = Mock()
        self.form_name_finder = Mock()
        self.dictionary_reader = Mock()
        self.browser_service = Mock()
        self.input_value = Mock()

    def create_brute_force_login(self):
        self.brute_force_login = \
            BruteForceLogin(self.args_dictionary,
                            self.message_administrator,
                            self.timer,
                            self.form_name_finder,
                            self.dictionary_reader,
                            self.browser_service)

    def set_return_values(self):
        self.form_name_finder.get_form_name.return_value = "login"
        self.dictionary_reader.read.return_value = ["royalcanin"]
        self.input_value.return_value = "admin"
        self.timer.get_minutes_elapsed.return_value = "15"

    def test_passwordIsFound_shouldPrintPasswordFound(self):
        EXPECTED_ANSWER = MessageAdministrator.PASSWORD_FOUND + \
                          self.MINUTES + \
                          MessageAdministrator.MINUTES + \
                          self.PASSWORD
        self.browser_service.verify_url_has_changed.return_value = True

        self.brute_force_login.execute()

        self.assertTrue(EXPECTED_ANSWER in self.mock_print.printed_answers)
        self.mock_print.delete_all_answers()

    def test_passwordIsNotFound_shouldPrintPasswordNotFound(self):
        EXPECTED_ANSWER = MessageAdministrator.PASSWORD + \
                            self.PASSWORD \
                            + MessageAdministrator.DIDNT_WORK
        self.browser_service.verify_url_has_changed.return_value = False

        self.brute_force_login.execute()

        self.assertTrue(EXPECTED_ANSWER in self.mock_print.printed_answers)
        self.mock_print.delete_all_answers()

    def test_noPasswordFound_shouldPrintUsernameUnsuccessful(self):
        EXPECTED_ANSWER = MessageAdministrator.USERS_PASSWORD \
                            + self.USERNAME \
                            + MessageAdministrator.NOT_FOUND
        self.browser_service.verify_url_has_changed.return_value = False

        self.brute_force_login.execute()

        print(self.mock_print.printed_answers)
        self.assertTrue(EXPECTED_ANSWER in self.mock_print.printed_answers)
        self.mock_print.delete_all_answers()


if __name__ == '__main__':
    unittest.main()

