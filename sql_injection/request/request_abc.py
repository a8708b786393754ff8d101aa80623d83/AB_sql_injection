import requests
from abc import ABC, abstractmethod


class RequestABC(ABC):
    """Classe abstraite pour les requetes 

    Args:
        ABC (ABCMeta): classe abs
    """

    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url
        self.payload = {}
        self.params = {}

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
    
    @abstractmethod
    def set_payload(self, data: dict, element: str) -> None: 
        """Ajoute est formatte les donées dans l'attributs payload

        Args:
            data (dict): données qui doivent etre stocké
            element (str): element 
        """

        for key, value in data.items(): 
            if value: 
                self.payload[key] = value
            else:
                self.payload[key] = element.strip()