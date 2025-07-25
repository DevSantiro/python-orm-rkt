from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetDeleterController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.pet_repository = pet_repository

    def delete_pet(self, name: str) -> dict:
        self.__delete_pet_from_db(name)

    def __delete_pet_from_db(self, name: str) -> None:
        try:
            self.pet_repository.delete_pets(name)

        except Exception as exception:
            raise exception
        