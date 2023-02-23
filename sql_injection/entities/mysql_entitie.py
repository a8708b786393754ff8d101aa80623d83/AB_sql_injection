from .entitie import Entitie


class MySQLEntitie(Entitie):
    """Entitée de MySQL

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        self.name = 'MySQL'
        super().__init__()

    def __del__(self) -> None:
        return super().__del__()
