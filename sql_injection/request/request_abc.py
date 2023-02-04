import requests
from abc import ABC, abstractmethod


class RequestABC(ABC):
    """Classe abstraite pour les requetes 

    Args:
        ABC (ABCMeta): classe abs
    """
    params: dict

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def request(self) -> requests.Response:
        """Renvoie la reponse de la requete

        Returns:
            requests.Response: _description_
        """

    @abstractmethod
    def set_params(self) -> None:
        """Ajoute les parametre dans l'attribut params."""
        
