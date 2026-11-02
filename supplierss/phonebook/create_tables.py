import psycopg2
from config import load_config

def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS contacts (
        contact_id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL UNIQUE,
        phone VARCHAR(20) NOT NULL UNIQUE
    );
    """

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
            conn.commit()
            print("Contacts table created!")

    except Exception as error:
        print(error)


if __name__ == '__main__':
    create_table()