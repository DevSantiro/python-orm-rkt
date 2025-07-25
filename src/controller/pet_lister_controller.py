from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetListerController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.pet_repository = pet_repository

    def list_pets(self):
        pets = self.__get_pets_in_db()
        return self.__format_response(pets)
    
    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.pet_repository.list_pets()
        return pets
    
    def __format_response(self, pets_info: list[PetsTable]) -> dict:
        return {
            "data": {
                "type": "Pets",
                "count": len(pets_info),
                "atributes": [
                    {
                        "name": pet.name,
                        "id": pet.id
                    } 
                    for pet in pets_info
                ]
            }
        }