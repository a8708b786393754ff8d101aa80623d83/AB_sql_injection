from abc import ABC, abstractmethod
from sql_injection.form import Form

import requests


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
        self.data = {}
        # NOTE contenue de la page de la premiere requete qui fait office de test pour savoir si l'injection est reussiste
        self.content_resp = self.request().content.decode()

    @abstractmethod
    def request(self) -> requests.Response:
        """Renvoie la reponse de la requete

        Returns:
            requests.Response: reponse de la requete
        """

    def set_data(self, form: Form, payload: str) -> None:
        """Ajoute est formatte les donées dans l'attributs data

        Args:
            form (Form): object Form 
            payload (str): payload sql 
        """

        self.data[form.username] = payload.strip()
        self.data[form.password] = 'aa'  # NOTE chaine au hashard

        for data in form.names:
            for key, value in data.items():
                if (key != form.username) and (key != form.password):
                    self.data[key] = value
