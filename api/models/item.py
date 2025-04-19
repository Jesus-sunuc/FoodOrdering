from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    id: Optional[int] = None
    item_name: str
    description: str
    price: float
    image_url: str
