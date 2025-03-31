from fastapi import APIRouter, Depends
from models.item import Item
from features.item.item_service import ItemService

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("")
def get_items(service: ItemService = Depends()):
    return service.get_items()


@router.post("")
def add_item(item: Item, service: ItemService = Depends()):
    return service.add_item(item)


@router.put("/{item_id}")
def update_item(item_id: str, item: Item, service: ItemService = Depends()):
    return service.update_item(item)


@router.delete("/{item_id}")
def delete_item(item_id: str, service: ItemService = Depends()):
    return service.delete_item(item_id)
