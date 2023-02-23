from .entitie import Entitie


class GenericEntitie(Entitie):
    """Entitée de Generic

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        self.name = 'Generic'
        super().__init__()

    def __del__(self) -> None:
        return super().__del__()
