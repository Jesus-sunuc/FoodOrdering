from fastapi import Depends
from services.database.connection import get_db_connection
from models.item import Item

class ItemRepository:
    def __init__(self, db=Depends(get_db_connection)):
        self.db = db

    def get_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM lunch_box.item")
        rows = cursor.fetchall()
        cursor.close()
        return rows


    def add(self, item: Item):
        self.db.execute(
            "INSERT INTO lunch_box.item (item_name, description, price, image_url) VALUES (?, ?, ?, ?)",
            (item.item_name, item.description, item.price, item.image_url),
        )
        self.db.commit()



    def update(self, item: Item):
        self.db.execute(
            "UPDATE lunch_box.item SET item_name=?, description=?, price=?, image_url=? WHERE id=?",
            (item.item_name, item.description, item.price, item.image_url, item.id),
        )
        self.db.commit()

    def delete(self, id: str):
        self.db.execute("DELETE FROM items WHERE id=?", (id,))
        self.db.commit()
