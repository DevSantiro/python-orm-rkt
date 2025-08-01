from abc import ABC, abstractmethod


class PersonFinderControllerInterface(ABC):
    @abstractmethod
    def find(self, person_id: int) -> dict: pass