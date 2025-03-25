from fastapi import Depends
from services.database.connection import get_db_connection
from models.item import Item

class ItemRepository:
    def __init__(self, db=Depends(get_db_connection)):
        self.db = db

    def get_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM lunch_box.items")
        rows = cursor.fetchall()
        cursor.close()
        return rows


    def add(self, item: Item):
        self.db.execute(
            "INSERT INTO items (id, title, description, image, price) VALUES (?, ?, ?, ?, ?)",
            (item.id, item.title, item.description, item.image, item.price),
        )
        self.db.commit()

    def update(self, item: Item):
        self.db.execute(
            "UPDATE items SET title=?, description=?, image=?, price=? WHERE id=?",
            (item.title, item.description, item.image, item.price, item.id),
        )
        self.db.commit()

    def delete(self, id: str):
        self.db.execute("DELETE FROM items WHERE id=?", (id,))
        self.db.commit()
