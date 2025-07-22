from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
import pytest

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection=db_connection_handler)
    response = repo.list_pets()
    print(response)
    

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_delete_pets():
    repo = PetsRepository(db_connection=db_connection_handler)
    repo.delete_pets(name="belinha")
    response = repo.list_pets()
    print(response)
    