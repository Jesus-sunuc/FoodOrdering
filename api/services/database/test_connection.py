import os
from dotenv import load_dotenv

load_dotenv()

import psycopg2
from psycopg2.extras import RealDictCursor


def get_test_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DB", "lunchbox_test"),
        user=os.getenv("POSTGRES_USER", "lunchbox"),
        password=os.getenv("POSTGRES_PASSWORD", "secret123"),
        cursor_factory=RealDictCursor,
    )
    return conn
