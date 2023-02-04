import bs4 

class Form(object):
    """Classe form, elle manie les fourmuliare

    Args:
        object (object): object
    """

    def __init__(self, form: bs4.BeautifulSoup) -> None: 
        self.form = form 

    @property
    def names(self) -> None: 
        """_summary_

        Returns:
            _type_: _description_
        """
        
        return self.form.selector('input[name]')

    @property
    def action(self) -> None: 
        """_summary_

        Returns:
            _type_: _description_
        """

        return self.form.selector('form[action]')        

    @property
    def method(self) -> None: 
        """_summary_

        Returns:
            _type_: _description_
        """

        return self.form.selector('form[method]')