class Entitie(object):
    """Entitée de base 

    Args:
        object (object): object python
    """

    def __init__(self) -> None:
        """Methode constructrice."""

        self.name = ''

    def get_name(self):
        """Renvoie le nom de l'entitée 

        Returns:
            str: nom bdd 
        """

        return self.name
