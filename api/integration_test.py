from api.services.database.test_connection import test_get_db_connection
import pytest
from fastapi.testclient import TestClient
from pydantic import BaseModel
from features.item.item_repository import ItemRepository
from main import app

client = TestClient(app)


class Item(BaseModel):
    id: str
    title: str
    description: str
    image: str
    price: float


@pytest.fixture(scope="module")
def dbconn():
    conn = test_get_db_connection()
    yield conn
    conn.close()


@pytest.fixture(scope="module")
def repo(dbconn):
    return ItemRepository(dbconn)