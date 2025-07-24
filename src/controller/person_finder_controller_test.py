from .person_finder_controller import PersonFinderController

class MockPerson():
    def __init__(self, first_name: str, last_name: str, pet_name: str, pet_type: str):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type

class MockPeopleRepository:
    def get_person(self, person_id: int):
        return MockPerson("John", "Doe", "Rex", "Dog")
    

def test_find():
    crontroller = PersonFinderController(MockPeopleRepository())
    response = crontroller.find(1)
    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "atributes": {
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "Rex",
                "pet_type": "Dog"
            }
        }
    }

    assert response == expected_response
    