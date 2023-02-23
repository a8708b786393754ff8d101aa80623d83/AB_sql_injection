from .entitie import Entitie


class PostgresSQLEntitie(Entitie):
    """Entitée de PostgresSQL

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        self.name = 'PostgresSQL'
        super().__init__()

    def __del__(self) -> None:
        return super().__del__()
