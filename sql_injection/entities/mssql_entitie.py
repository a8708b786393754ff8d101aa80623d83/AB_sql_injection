from .entitie import Entitie


class MSSQLEntitie(Entitie):
    """Entitée de MSSQL

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = 'MSSQL'

    def __del__(self) -> None:
        return super().__del__()
