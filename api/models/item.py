from pydantic import BaseModel


class Item(BaseModel):
    id: str
    title: str
    description: str
    image: str
    price: float
