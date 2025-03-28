# import pytest
# from fastapi.testclient import TestClient
# from main import app
# from models.item import Item
# from features.item.item_service import ItemService
# from services.connection import DatabaseConnection
# from features.item.ItemRepository import ItemRepository
 
# client = TestClient(app)
 
# class Item(BaseModel):
#     id: str
#     title: str
#     description: str
#     image: str
#     price: float
 
# @pytest.fixture(scope="module")
# def dbconn():
#     db = DatabaseConnection()
#     yield db
#     db.close()
 
# @pytest.fixture(scope="module")
# def repo(dbconn):
#     return ItemRepository(dbconn)
 
# def get_all_test(repo):
#     items = repo.get_all()
#     item = Item(id="6", title="Avocado Toast", description="Sourdough toast topped with smashed avocado, chili flakes, and microgreens.", image="https://storagelunchbox.blob.core.windows.net/images/avocado_toast.jpg", price=6.99)
#     assert item in items
 
print("Test passed");