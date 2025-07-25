from abc import ABC, abstractmethod


class PetDeleterControllerInterface(ABC):
    @abstractmethod
    def delete_pet(self, name: str) -> None: pass
        