from os.path import exists


class DictionaryReader:
    dictionaries_root = "Dictionaries\\"
    dict_name = ''

    def __init__(self, dict_name):
        self.dict_name = dict_name

    def read(self):
        path = self.dictionaries_root + self.dict_name
        passwords = []
        if exists(path):
            with (open(path)) as dict:
                for line in dict:
                    password = line.rstrip("\n")  # On enlève le retour de chariot de chaque ligne
                    passwords.append(password)
        else:
            print("Dictionaire introuvable...")

        return passwords




