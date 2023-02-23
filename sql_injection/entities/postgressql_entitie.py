from .entitie import Entitie


class PostgresSQLEntitie(Entitie):
    """Entitée de PostgresSQL

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = 'PostgresSQL'

    def __del__(self) -> None:
        return super().__del__()
