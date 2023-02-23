import bs4


class Form(object):
    """Classe form, elle manie les fourmuliare

    Args:
        object (object): object
    """

    NAMES_USER = ['username', 'email', 'nom_utilisateur',
                  'session_key', 'session_username', 'session_user']
    NAMES_PASSWORD = ['password', 'passwd', 'pass', 'motdepasse',
                      'session_password', 'session_passwd', 'session_pass']

    def __init__(self, form: bs4.BeautifulSoup) -> None:
        """Méthode constructrice

        Args:
            form (bs4.BeautifulSoup): soup du formulaire
        """

        self.form = form
        self.password = ''
        self.username = ''

        self.__set_credentials()

    def __set_credentials(self) -> None:
        """Methode privée pour ajoutée les name de connexion a leurs attribut."""

        for element in self.names:
            for key in element.keys():
                if key in self.NAMES_USER:
                    self.username = key
                elif key in self.NAMES_PASSWORD:
                    self.password = key

    @property
    def names(self) -> list[dict]:
        """Renvoie une liste qui contient des dictionnaire avec le name est sa valeur trouvée dans le formulaire

        Returns:
            list[dict]: liste de dictionnaire
        """

        names = []
        for input in self.form.select('input'):
            names.append({input.get('name'): input.get('value')})

        return names

    @property
    def action(self) -> str:
        """Renvoie l'action du formulaire

        Returns:
            str: action du formulaire
        """

        return self.form.get('action')

    @property
    def method(self) -> str:
        """Renvoie les methode du formulaire

        Returns:
            str: methode d'envoie
        """

        return self.form.get('method')
