import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, person_info: dict) -> dict:
        first_name = person_info.get("first_name")
        last_name = person_info.get("last_name")
        age = person_info.get("age")
        pet_id = person_info.get("pet_id")

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        formated_response = self.__format_response(person_info)
        return formated_response

    def __validate_first_and_last_name(self, first_name: str, last_name: str):
        non_valid_caracteres = re.compile(r"[^a-zA-Z]")
        
        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
            raise ValueError("First name contains invalid characters.")
        
    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "atributes": person_info
            }
        }