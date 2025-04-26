import pytest
from fastapi.testclient import TestClient
from pydantic import BaseModel
from features.item.item_repository import ItemRepository
from services.database.connection import get_db_connection
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
    conn = get_db_connection()
    yield conn
    conn.close()


@pytest.fixture(scope="module")
def repo(dbconn):
    return ItemRepository(dbconn)


def test_get_items():
    response = client.get("api/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "item_name" in data[0]
        assert "price" in data[0]


def test_add_item():
    new_item = {
        "id": "7",
        "item_name": "Test Sandwich",
        "description": "Just a test",
        "price": 4.50,
        "image_url": "https://example.com/test.jpg",
    }

    response = client.post("api/items", json=new_item)
    assert response.status_code == 200 or response.status_code == 201


def test_update_item():
    updated_data = {
        "id": "7",
        "item_name": "Updated Toast",
        "description": "Updated desc",
        "price": 7.25,
        "image_url": "https://example.com/updated.jpg",
    }

    response = client.put("api/items/7", json=updated_data)
    assert response.status_code != 200 # logic reversed to make tests fail


def test_delete_item():
    item_id = "7"
    response = client.delete(f"api/items/{item_id}")
    assert response.status_code == 200