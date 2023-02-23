from .entitie import Entitie


class MSSQLEntitie(Entitie):
    """Entitée de MSSQL

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        self.name = 'MSSQL'
        super().__init__()

    def __del__(self) -> None:
        return super().__del__()
