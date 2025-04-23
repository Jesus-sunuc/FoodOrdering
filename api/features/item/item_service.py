from fastapi import Depends
from models.item import Item
from features.item.item_repository import ItemRepository


class ItemService:
    def __init__(self, repo: ItemRepository = Depends()):
        self.repo = repo

    def get_items(self):
        return self.repo.get_all()

    def add_item(self, item: Item):
        self.repo.add_item(item)
        return item 

    def update_item(self, item: Item):
        return self.repo.update_item(item)

    def delete_item(self, item_id: str):
        return self.repo.delete_item(item_id)
