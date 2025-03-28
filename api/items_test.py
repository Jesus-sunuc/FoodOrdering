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
