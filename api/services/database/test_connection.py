import os
from dotenv import load_dotenv

load_dotenv()

import psycopg2
from psycopg2.extras import RealDictCursor


def test_get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="lunchbox_test",
        user="lunchbox",
        password="secret123",
        cursor_factory=RealDictCursor,
    )
    return conn