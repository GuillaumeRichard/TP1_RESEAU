import os
from src.exceptions.DictionaryNotFoundError import DictionaryNotFoundError
from src.MessageAdministrator import MessageAdministrator

class DictionaryReader:
    dictionaries_root = os.getcwd() + "\\Dictionaries\\"
    dict_name = ''

    def __init__(self, dict_name):
        self.dict_name = dict_name

    def read(self):
        path = self.dictionaries_root + self.dict_name
        passwords = []
        if os.path.isfile(path):
            with (open(path)) as dictionary:
                for line in dictionary:
                    password = line.rstrip("\n")  # On enlève le retour de chariot de chaque ligne
                    passwords.append(password)
        else:
            message = MessageAdministrator.get_dict_not_found_message(path)
            raise DictionaryNotFoundError(message)

        return passwords




