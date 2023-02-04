import requests
from abc import ABC, abstractmethod


class RequestABC(ABC):
    """Classe abstraite pour les requetes 

    Args:
        ABC (ABCMeta): classe abs
    """
    params: dict
    url: str

    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    @abstractmethod
    def request(self) -> requests.Response:
        """Renvoie la reponse de la requete

        Returns:
            requests.Response: _description_
        """

    @abstractmethod
    def set_params(self, data: dict) -> None:
        """Ajoute les parametre dans l'attribut params."""

        for key, value in data.items():
            if key in self.params:
                self.params[key] += value
            else:
                self.params[key] = value
        
