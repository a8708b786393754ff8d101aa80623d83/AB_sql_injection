import bs4


class Form(object):
    """Classe form, elle manie les fourmuliare

    Args:
        object (object): object
    """

    def __init__(self, form: bs4.BeautifulSoup) -> None:
        self.form = form

    def __str__(self) -> str:
        return self.form.__str__()

    @property
    def names(self) -> list[str]:
        """Renvoie une liste de name trouvée dans le formulaire

        Returns:
            list[str]: liste de name
        """

        names = []
        for input in self.form.select('input'):
            names.append(input.name)

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
