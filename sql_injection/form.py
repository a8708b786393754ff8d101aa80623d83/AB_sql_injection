import bs4


class Form(object):
    """Classe form, elle manie les fourmuliare

    Args:
        object (object): object
    """
    NAMES_USER = ['username', 'email', 'nom_utilisateur', 'session_key', 'session_username', 'session_user']
    NAMES_PASSWORD = ['password', 'passwd', 'pass', 'motdepasse', 'session_password', 'session_passwd', 'session_pass']

    def __init__(self, form: bs4.BeautifulSoup) -> None:
        self.form = form
        self.password = ''
        self.username = ''

        self.__set_credentials()
        

    def __str__(self) -> str:
        return self.form.__str__()

    @property
    def names(self) -> list[dict]:
        """Renvoie une liste de tuple avec le name est sa valeur trouvée dans le formulaire

        Returns:
            list[str]: liste de name
        """

        names = []
        for input in self.form.select('input'):
            names.append({input.get('name'): input.get('value')})

        return names

    @property
    def action(self) -> str:
        """Renvoie l'action du formulaire

        Returns:
            str|list: action
        """

        return self.form.get('action')

    @property
    def method(self) -> str:
        """Renvoie les methode du formulaire

        Returns:
            str|list: method
        """

        return self.form.get('method')

    def __set_credentials(self) -> None:
        """Methode privée pour ajoutée les name de connexion a leurs attribut."""

        for element in self.names:
            for key in element.keys():
                if key in self.NAMES_USER:
                    self.username = key
                elif key in self.NAMES_PASSWORD:
                    self.password = key
