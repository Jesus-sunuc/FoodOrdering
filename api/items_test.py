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


def test_get_all(repo):
    db_rows = repo.get_all()

    items = [
        Item(
            id=str(row["id"]),
            title=row["item_name"],
            description=row["description"],
            image=row["image_url"],
            price=float(row["price"]),
        )
        for row in db_rows
    ]

    expected_item = Item(
        id="6",
        title="Avocado Toast",
        description="Sourdough toast topped with smashed avocado, chili flakes, and microgreens.",
        image="https://storagelunchbox.blob.core.windows.net/images/avocado_toast.jpg",
        price=6.99,
    )

    assert expected_item in items


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

    response = client.put(f"api/items/7", json=updated_data)
    assert response.status_code == 200


def test_delete_item():
    item_id = "7"
    response = client.delete(f"api/items/{item_id}")
    assert response.status_code == 200
