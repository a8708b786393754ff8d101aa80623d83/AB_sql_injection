from .entitie import Entitie


class OracleEntitie(Entitie):
    """Entitée de Oracle

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        self.name = 'Oracle'
        super().__init__()

    def __del__(self) -> None:
        return super().__del__()
