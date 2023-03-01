from sql_injection.request.request_abc import RequestABC
from requests import Response


class Injection(object):
    def __init__(self, error: str | None) -> None:
        self.error = error

    def successful(self, req: RequestABC, resp: Response) -> bool:
        """Verifie si le contenue de la page sans paylaod est la meme que celle avec le payload, 
            si c'est pas la meme,c'est que l'injection a reussi

        Args:
            req (RequestABC): object requestabc
            resp (Response): object reponse

        Returns:
            bool: True si la reponse avec le payload n'est pas la meme que sans payload, False si c'est la meme
        """

        if resp.ok:
            if self.error:
                return not self.error in resp.content.decode()