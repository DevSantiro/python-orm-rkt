from abc import ABC, abstractmethod

class PeopleRepositoryInterface(ABC):
    @abstractmethod
    def get_person(self, person_id: int): pass
    
    @abstractmethod
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int): pass
    