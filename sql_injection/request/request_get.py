from .request_abc import RequestABC
import requests  # lib PyPi requests


class RequestGet(RequestABC):
    """Classe pour les requete en GET

    Args:
        RequestABC (object): classe mere
    """

    def __init__(self, url: str) -> None:
        super().__init__(url)

    def request(self) -> requests.Response:
        return requests.get(self.url, params=self.data, verify=True)
