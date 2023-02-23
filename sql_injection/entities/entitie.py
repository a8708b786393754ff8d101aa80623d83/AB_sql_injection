class Entitie(object):
    """Entitée de base 

    Args:
        object (object): object python
    """

    def __init__(self) -> None:
        """Methode constructrice."""

        self.name: str
        self.f = open(self.name)

    def get_name(self) -> str:
        """Renvoie le nom de l'entitée 

        Returns:
            str: nom bdd 
        """

        return self.name

    def get_payload(self) -> str:
        """Renvoie la ligne suivante du payload

        Returns:
            str: payload
        """

        return self.f.readline().strip()

    def __del__(self) -> None:
        """Méthode destructrice, ferme le fichier."""

        self.f.close()
