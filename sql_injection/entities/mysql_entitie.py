from .entitie import Entitie


class MySQLEntitie(Entitie):
    """Entitée de MySQL

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = 'MySQL'

    def __del__(self) -> None:
        return super().__del__()
