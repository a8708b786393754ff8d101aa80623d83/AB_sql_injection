from .request_abc import RequestABC
import requests  # lib PyPi requests


class RequestPost(RequestABC):
    """Classe pour les requete en post

    Args:
        RequestABC (object): classe mere
    """

    def __init__(self, url: str) -> None:
        super().__init__(url)

    def request(self) -> requests.Response:
        return requests.post(self.url, data=self.payload, verify=True)

    def set_payload(self, form, entitie) -> None:
        return super().set_payload(form, entitie)
