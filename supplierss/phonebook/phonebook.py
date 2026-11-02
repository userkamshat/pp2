import psycopg2
import csv
from config import load_config
#4.1

def insert_from_csv(filename):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, 'r') as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        cur.execute(
                            """
                            INSERT INTO contacts (username, phone)
                            VALUES (%s, %s)
                            ON CONFLICT DO NOTHING
                            """,
                            (row['username'], row['phone'])
                        )

            conn.commit()

        print("CSV contacts imported!")

    except Exception as error:
        print(error)

#4.2
def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO contacts (username, phone)
                    VALUES (%s, %s)
                    """,
                    (username, phone)
                )

            conn.commit()

        print("Contact added!")

    except Exception as error:
        print(error)

#4.3
def update_username(old_username, new_username):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE contacts
                    SET username = %s
                    WHERE username = %s
                    """,
                    (new_username, old_username)
                )

                print("Updated rows:", cur.rowcount)

            conn.commit()

    except Exception as error:
        print(error)

#4.4
def update_phone(username, new_phone):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE contacts
                    SET phone = %s
                    WHERE username = %s
                    """,
                    (new_phone, username)
                )

                print("Updated rows:", cur.rowcount)

            conn.commit()

    except Exception as error:
        print(error)

#4.5
def search_by_name(name):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM contacts
                    WHERE username ILIKE %s
                    """,
                    ('%' + name + '%',)
                )

                rows = cur.fetchall()

                for row in rows:
                    print(row)

    except Exception as error:
        print(error)


#4.6
def search_by_phone_prefix(prefix):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM contacts
                    WHERE phone LIKE %s
                    """,
                    (prefix + '%',)
                )

                rows = cur.fetchall()

                for row in rows:
                    print(row)

    except Exception as error:
        print(error)
#4.7
def delete_by_username(username):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM contacts WHERE username = %s",
                    (username,)
                )

                print("Deleted rows:", cur.rowcount)

            conn.commit()

    except Exception as error:
        print(error)
#4.8
def delete_by_phone(phone):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM contacts WHERE phone = %s",
                    (phone,)
                )

                print("Deleted rows:", cur.rowcount)

            conn.commit()

    except Exception as error:
        print(error)


if __name__ == '__main__':

    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Import contacts from CSV")
        print("2. Add contact")
        print("3. Update username")
        print("4. Update phone")
        print("5. Search by name")
        print("6. Search by phone prefix")
        print("7. Delete by username")
        print("8. Delete by phone")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            insert_from_csv("contacts.csv")

        elif choice == '2':
            insert_from_console()

        elif choice == '3':
            old_name = input("Enter old username: ")
            new_name = input("Enter new username: ")
            update_username(old_name, new_name)

        elif choice == '4':
            username = input("Enter username: ")
            new_phone = input("Enter new phone: ")
            update_phone(username, new_phone)

        elif choice == '5':
            name = input("Enter name to search: ")
            search_by_name(name)

        elif choice == '6':
            prefix = input("Enter phone prefix: ")
            search_by_phone_prefix(prefix)

        elif choice == '7':
            username = input("Enter username to delete: ")
            delete_by_username(username)

        elif choice == '8':
            phone = input("Enter phone to delete: ")
            delete_by_phone(phone)

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")