from abc import ABC, abstractmethod

import requests
from sql_injection.entities.entitie import Entitie
from sql_injection.form import Form


class RequestABC(ABC):
    """Classe abstraite pour les requetes 

    Args:
        ABC (ABCMeta): classe abs
    """

    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url
        self.payload = {}

    @abstractmethod
    def request(self) -> requests.Response:
        """Renvoie la reponse de la requete

        Returns:
            requests.Response: _description_
        """

    @abstractmethod
    def set_payload(self, form: Form, entitie: Entitie) -> None:
        """Ajoute est formatte les donées dans l'attributs payload

        Args:
            data (dict): données qui doivent etre stocké
            element (str): element 
        """
        
        payload = entitie.get_payload()

        self.payload[form.username] = payload
        self.payload[form.password] = payload

        for data in form.names:
            for key, value in data.items():
                if (key != form.username) and (key != form.password):
                    self.payload[key] = value
