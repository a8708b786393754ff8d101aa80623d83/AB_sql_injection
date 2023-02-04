import bs4 

class Form(object):
    """Classe form, elle manie les fourmuliare

    Args:
        object (object): object
    """

    def __init__(self, form: bs4.BeautifulSoup) -> None: 
        self.form = form 

    @property
    def names(self) -> list[str]: 
        """Renvoie une liste de name trouvée dans le formulaire

        Returns:
            list[str]: liste de name
        """

        names = []
        for input in  self.form.select('input'): 
            names.append(input.name)
        
        return names 

    @property
    def action(self) -> str|list: 
        """Renvoie l'action du formulaire

        Returns:
            str|list: action
        """

        return self.form.find_all('input').action        

    @property
    def method(self) -> None: 
        """_summary_

        Returns:
            _type_: _description_
        """

        return self.form.selector('form[method]')