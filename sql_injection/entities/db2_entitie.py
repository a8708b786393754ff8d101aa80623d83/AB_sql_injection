from .entitie import Entitie


class Db2Entitie(Entitie):
    """Entitée de Db2

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = 'Db2'

    def __del__(self) -> None:
        return super().__del__()
