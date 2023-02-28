from abc import ABC, abstractmethod

import requests
from sql_injection.form import Form


class RequestABC(ABC):
    """Classe abstraite pour les requetes 

    Args:
        ABC (ABCMeta): classe abs
    """

    def __init__(self, url: str) -> None:
        """Méthode constructrice

        Args:
            url (str): url du site
        """

        super().__init__()
        self.url = url
        self.payload = {}

    @abstractmethod
    def request(self) -> requests.Response:
        """Renvoie la reponse de la requete

        Returns:
            requests.Response: reponse de la requete
        """

    @abstractmethod
    def set_payload(self, form: Form, payload: str) -> None:
        """Ajoute est formatte les donées dans l'attributs payload

        Args:
            form (Form): object Form 
            payload (str): payload sql 
        """

        self.payload[form.username] = payload.strip()
        self.payload[form.password] = 'aa' #NOTE chaine au hashard

        for data in form.names:
            for key, value in data.items():
                if (key != form.username) and (key != form.password):
                    self.payload[key] = value
