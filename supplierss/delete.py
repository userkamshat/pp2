import psycopg2
from config import load_config

def delete_part(part_id):
    """Delete part by part id"""

    rows_deleted = 0

    sql = "DELETE FROM parts WHERE part_id = %s"

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(sql, (part_id,))

                rows_deleted = cur.rowcount

            conn.commit()

    except Exception as error:
        print(error)

    return rows_deleted


if __name__ == '__main__':
    deleted_rows = delete_part(2)
    print("The number of deleted rows:", deleted_rows)