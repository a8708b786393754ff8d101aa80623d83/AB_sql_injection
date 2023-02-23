from .entitie import Entitie


class GenericEntitie(Entitie):
    """Entitée de Generic

    Args:
        Entitie (object): entitée de base
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = 'Generic'

    def __del__(self) -> None:
        return super().__del__()
