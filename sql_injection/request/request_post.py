import requests  # lib PyPi requests

from .request_abc import RequestABC


class RequestPost(RequestABC):
    """Classe pour les requete en post

    Args:
        RequestABC (object): classe mere
    """

    def __init__(self, url: str) -> None:
        super().__init__(url)

    def request(self) -> requests.Response:
        return requests.post(self.url, data=self.data, verify=True)
