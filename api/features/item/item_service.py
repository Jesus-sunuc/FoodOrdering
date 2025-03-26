from fastapi import Depends
from models.item import Item
from features.item.item_repository import ItemRepository


class ItemService:
    def __init__(self, repo: ItemRepository = Depends()):
        self.repo = repo

    def get_items(self):
        return self.repo.get_all()

    def add_item(self, item: Item):
        self.repo.add(item)

    def update_item(self, item: Item):
        self.repo.update(item)

    def delete_item(self, id: str):
        self.repo.delete(id)
