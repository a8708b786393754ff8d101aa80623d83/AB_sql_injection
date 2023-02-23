from pathlib import Path


class Entitie(object):
    """Entitée de base 

    Args:
        object (object): object python
    """

    DETECT = 'detect/'
    SQL_BLIND = 'payloads-sql-blind/'
    PAYLOAD = 'payloads/'

    def __init__(self, blind: bool = False) -> None:
        """Methode constructrice.


        Args:
            blind (bool, optional): pour les injection cachée. Defaults to False.

        Raises:
            FileNotFoundError: fichier non trouvée
        """

        
        self.name: str
        #FIXME ajout liste de fichier est le regroupement du contenue des fichiers

        if blind:
            file = Path(self.PAYLOAD + self.SQL_BLIND + self.name)
        else:
            file = Path(self.PAYLOAD + self.DETECT + self.name)

        

        if file.exists() and file: 
            self.f = file.open()
        else: 
            raise FileNotFoundError()


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
