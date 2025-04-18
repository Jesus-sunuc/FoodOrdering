from services.database.test_connection import test_get_db_connection
import pytest
from httpx import AsyncClient
import httpx 
from main import app
from models.item import Item
from services.database.connection import get_db_connection

@pytest.fixture(scope="module", autouse=True)
def override_db():
    app.dependency_overrides[get_db_connection] = test_get_db_connection
    yield
    app.dependency_overrides.clear()

@pytest.mark.asyncio
async def test_add_get_delete_item():
    async with AsyncClient(base_url="http://test", transport=httpx.ASGITransport(app=app)) as client:
        item_data = {
            "id": "test-id-1",
            "item_name": "Test Item",
            "description": "A test description",
            "price": 5.99,
            "image_url": "http://example.com/image.png"
        }

        response = await client.post("/api/items", json=item_data)
        assert response.status_code == 200

        response = await client.get("/api/items")
        assert response.status_code == 200
        items = response.json()
        assert any(i["id"] == "test-id-1" for i in items)

        response = await client.delete("/api/items/test-id-1")
        assert response.status_code == 200
