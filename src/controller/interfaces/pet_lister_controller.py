from abc import ABC, abstractmethod
from src.models.sqlite.entities.pets import PetsTable


class PetListerControllerInterface(ABC):
    @abstractmethod
    def list_pets(self) -> list[PetsTable]: pass
    