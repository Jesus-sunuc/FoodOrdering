from pydantic import BaseModel


class Item(BaseModel):
    id: str
    item_name: str
    description: str
    price: float
    image_url: str
