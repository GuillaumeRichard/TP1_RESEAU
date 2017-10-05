def print_message(message):
    print(message)


class MessageAdministrator:
    ENTER_USERNAME = "Entrez le nom de l'utilisateur pour qui vous voulez trouver le mot de passe: "
    PASSWORD_FOUND = "Mot de passe trouvé en "
    MINUTES = " minutes: "
    USERS_PASSWORD = "Le mot de passe de l'utilisateur "
    NOT_FOUND = " n\'a pas été trouvé"
    PASSWORD = "Le mot de passe "
    DIDNT_WORK = " n\'a pas fonctionné..."

    def __init__(self):
        self.print_function = print_message

    @staticmethod
    def get_url_not_found_message(url):
        return "L'url " + url + " n\'a pas été trouvé"

    @staticmethod
    def get_dict_not_found_message(path):
        return "Le dictionaire situé au chemin " + path + " n\'a pas été trouvé"

    @staticmethod
    def get_form_not_found_message(user_field, password_field):
        return "Le formulaire avec le nom de champ d\'utilisateur \'" + user_field + "\'\n " \
                "et le nom de champ de mot de passe \'" + password_field + "\'\n " \
                "n\'a pas été trouvé"

    def print_username_not_found(self, username):
        self.print_function(MessageAdministrator.USERS_PASSWORD
                            + username
                            + MessageAdministrator.NOT_FOUND)

    def print_password_found(self, minutes_elapsed, password):
        self.print_function(MessageAdministrator.PASSWORD_FOUND
                            + minutes_elapsed
                            + MessageAdministrator.MINUTES
                            + password)

    def print_password_unsuccessful(self, password):
        self.print_function(MessageAdministrator.PASSWORD
                            + password
                            + MessageAdministrator.DIDNT_WORK)

