from .entitie import Entitie


class OracleEntitie(Entitie):
    """Entitée de Oracle

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = 'Oracle'

    def __del__(self) -> None:
        return super().__del__()
