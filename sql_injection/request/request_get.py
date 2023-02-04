from request.request_abc import RequestABC
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

        super().__init__()
        print(self.url)

    def request(self) -> requests.Response:
        return requests.get(self.url, params=self.params, verify=True)

    def set_params(self, data: dict) -> None:
        return super().set_params(data)
