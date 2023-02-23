from .entitie import Entitie


class NoSQLEntitie(Entitie):
    """Entitée de NoSQL

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = 'NoSQL'

    def __del__(self) -> None:
        return super().__del__()
