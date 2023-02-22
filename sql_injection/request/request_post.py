from .request_abc import RequestABC
import requests # lib PyPi requests

class RequestPost(RequestABC): 
    """_summary_

    Args:
        RequestABC (_type_): _description_
    """

    def __init__(self, url: str) -> None:
        super().__init__(url)

    def request(self) -> requests.Response:
        return requests.post(self.url, data=self.payload, verify=True)

    def set_payload(self, data: dict, element: str) -> None: 
        return super().set_params(data, element)
