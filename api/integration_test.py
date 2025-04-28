from services.database.test_connection import get_test_db_connection
import pytest
from httpx import AsyncClient
import httpx
from main import app
from services.database.connection import get_db_connection


@pytest.fixture(scope="module", autouse=True)
def override_db():
    app.dependency_overrides[get_db_connection] = get_test_db_connection
    yield
    app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_add_get_delete_item():
    async with AsyncClient(
        base_url="http://test", transport=httpx.ASGITransport(app=app)
    ) as client:
        item_data = {
            "item_name": "Test Item",
            "description": "A test description",
            "price": 5.99,
            "image_url": "http://example.com/image.png",
        }

        # Add item
        response = await client.post("/api/items", json=item_data)
        assert response.status_code == 200

        # Get items
        response = await client.get("/api/items")
        assert response.status_code == 200
        items = response.json()

        # Assert it was added
        matching_item = next((i for i in items if i["item_name"] == "Test Item"), None)
        assert matching_item is not None

        # Delete the item using its auto-generated ID
        response = await client.delete(f"/api/items/{matching_item['id']}")
        assert response.status_code == 200
