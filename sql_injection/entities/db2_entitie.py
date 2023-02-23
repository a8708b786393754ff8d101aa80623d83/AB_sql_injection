from .entitie import Entitie


class Db2Entitie(Entitie):
    """Entitée de Db2

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        self.name = 'Db2'
        super().__init__()

    def __del__(self) -> None:
        return super().__del__()
