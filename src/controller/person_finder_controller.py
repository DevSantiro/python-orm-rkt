from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonFinderController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response
    
    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)

        if not person:
            raise Exception("Person not found.")

        return person
    
    def __format_response(self, person_info: PeopleTable) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "atributes": {
                    "first_name": person_info.first_name,
                    "last_name": person_info.last_name,
                    "pet_name": person_info.pet_name,
                    "pet_type": person_info.pet_type
                }
            }
        }