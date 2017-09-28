from os.path import exists
import sys
from Messages import Messages


class DictionaryReader:
    dictionaries_root = "Dictionaries\\"
    dict_name = ''

    def __init__(self, dict_name):
        self.dict_name = dict_name

    def read(self):
        path = self.dictionaries_root + self.dict_name
        passwords = []
        if exists(path):
            with (open(path)) as dictionary:
                for line in dictionary:
                    password = line.rstrip("\n")  # On enlève le retour de chariot de chaque ligne
                    passwords.append(password)
        else:
            print(Messages.DICTIONARY_NOT_FOUND)
            sys.exit(1)

        return passwords




