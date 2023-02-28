from pathlib import Path
from sql_injection.utils import listing_path


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

        if blind:
            file = Path(self.PAYLOAD + self.SQL_BLIND + self.name + '_blind.txt')
        else:
            file = Path(self.PAYLOAD + self.DETECT + self.name + '.txt')


        if file.exists() and file.is_file(): 
            self.f = file.open()
        else: 
            raise FileNotFoundError()


    def get_name(self) -> str:
        """Renvoie le nom de l'entitée 

        Returns:
            str: nom bdd 
        """

        return self.name

    @property
    def payloads(self) -> list:
        """Renvoie les payloads

        Returns:
            list: payloads
        """
        
        return self.f.readlines()

    def __del__(self) -> None:
        """Méthode destructrice, ferme le fichier."""

        self.f.close()
