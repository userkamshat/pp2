import json
from connect import connect_db


# 1. Search contacts
def search_contacts(pattern):

    with connect_db() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "SELECT * FROM search_contacts(%s)",
                (pattern,)
            )

            rows = cur.fetchall()

            for row in rows:
                print(row)


# 2. Insert or update contact
def upsert_contact(username, phone):

    with connect_db() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "CALL upsert_contact(%s, %s)",
                (username, phone)
            )

            print("Contact saved!")


# 3. Insert many contacts
def insert_many_contacts(contacts):

    with connect_db() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "CALL insert_many_contacts(%s::JSONB, NULL)",
                (json.dumps(contacts),)
            )

            invalid_data = cur.fetchone()[0]

            print("Incorrect contacts:")
            print(invalid_data)


# 4. Get contacts using pagination
def get_contacts_page(limit, offset):

    with connect_db() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "SELECT * FROM get_contacts_page(%s, %s)",
                (limit, offset)
            )

            rows = cur.fetchall()

            for row in rows:
                print(row)


# 5. Delete contact
def delete_contact(value, delete_type):

    with connect_db() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "CALL delete_contact(%s, %s)",
                (value, delete_type)
            )

            print("Delete operation completed!")


# Main menu
def main():

    while True:

        print("\n===== PHONEBOOK =====")
        print("1. Search contacts")
        print("2. Insert or update contact")
        print("3. Insert many contacts")
        print("4. Show contacts by pages")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            pattern = input("Enter name or phone: ")
            search_contacts(pattern)

        elif choice == "2":

            username = input("Enter username: ")
            phone = input("Enter phone: ")

            upsert_contact(username, phone)

        elif choice == "3":

            contacts = [
                {"username": "Ali", "phone": "87001234567"},
                {"username": "Aruzhan", "phone": "87771234567"},
                {"username": "John", "phone": "abc123"},
                {"username": "Diana", "phone": "123"}
            ]

            insert_many_contacts(contacts)

        elif choice == "4":

            limit = int(input("How many contacts per page? "))
            offset = int(input("Enter offset: "))

            get_contacts_page(limit, offset)

        elif choice == "5":

            delete_type = input("Delete by username or phone? ")
            value = input("Enter value: ")

            delete_contact(value, delete_type)

        elif choice == "0":

            print("Goodbye!")
            break

        else:

            print("Invalid choice!")


if __name__ == "__main__":
    main()