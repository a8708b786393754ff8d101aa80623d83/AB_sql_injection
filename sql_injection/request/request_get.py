from .request_abc import RequestABC
import requests  # lib PyPi requests


class RequestGet(RequestABC):
    """_summary_

    Args:
        RequestABC (_type_): _description_
    """

    def __init__(self, url: str) -> None:
        """Méthode constructrice.

        Args:
            url (str): url
        """

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
