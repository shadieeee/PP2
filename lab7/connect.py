import psycopg2
from config import get_db_config

def connect():
    try:
        params = get_db_config()
        conn = psycopg2.connect(**params)
        return conn
    except Exception as error:
        print(f"Ошибка подключения: {error}")
        return None