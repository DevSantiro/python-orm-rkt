from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController


class MockPetsRepository:
    def list_pets(self) -> list[PetsTable]:
        list_of_pets = [
            PetsTable(id=1, name="Buddy", type="Dog"),
            PetsTable(id=2, name="Mittens", type="Cat"),
            PetsTable(id=3, name="Goldie", type="Fish")
        ]

        return list_of_pets
    
def test_list_pets():
    mock_repository = MockPetsRepository()
    controller = PetListerController(mock_repository)
    response = controller.list_pets()
    expected_response = {
        "data": {
            "type": "Pets",
            "count": 3,
            "atributes": [
                {"name": "Buddy", "id": 1},
                {"name": "Mittens", "id": 2},
                {"name": "Goldie", "id": 3}
            ]
        }
    }

    assert response == expected_response
