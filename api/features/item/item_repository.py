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

    def add_item(self, item: Item):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO lunch_box.item (item_name, description, price, image_url)
            VALUES (%s, %s, %s, %s)
            """,
            (item.item_name, item.description, item.price, item.image_url),
        )
        self.db.commit()
        cursor.close()

    def update_item(self, item: Item):
        cursor = self.db.cursor()
        cursor.execute(
            """
            UPDATE lunch_box.item
            SET item_name=%s, description=%s, price=%s, image_url=%s
            WHERE id=%s
            """,
            (item.item_name, item.description, item.price, item.image_url, item.id),
        )
        self.db.commit()
        cursor.close()

    def delete_item(self, item_id: str):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM lunch_box.item WHERE id = %s", (item_id,))
        self.db.commit()
        cursor.close()
