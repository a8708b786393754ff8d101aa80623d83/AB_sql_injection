from .request_abc import RequestABC
import requests  # lib PyPi requests


class RequestGet(RequestABC):
    """Classe pour les requete en GET

    Args:
        RequestABC (object): classe mere
    """

    def __init__(self, url: str) -> None:
        super().__init__(url)

        self.params = {}

    def request(self) -> requests.Response:
        return requests.get(self.url, params=self.params, data=self.payload, verify=True)

    def set_params(self, data: dict) -> None:
        """Ajoute les parametre dans l'attribut params."""

        for key, value in data.items():
            if key in self.params:
                self.params[key] += value
            else:
                self.params[key] = value
