
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


# 6. Advanced search, filter and sort
def advanced_search():

    group_name = input("Enter group (Family/Work/Friend/Other or all): ")
    email_query = input("Enter email search (or press Enter to skip): ")

    print("\nSort by:")
    print("1. Name")
    print("2. Birthday")
    print("3. Date added")

    sort_choice = input("Choose sorting: ")

    if sort_choice == "1":
        sort_column = "c.username"
    elif sort_choice == "2":
        sort_column = "c.birthday"
    elif sort_choice == "3":
        sort_column = "c.created_at"
    else:
        sort_column = "c.username"

    page_size = 2
    page = 0

    while True:

        offset = page * page_size

        query = """
            SELECT
                c.username,
                c.email,
                c.birthday,
                g.name AS contact_group,
                COALESCE(c.phone, '') ||
                CASE
                    WHEN COUNT(p.id) > 0
                    THEN ', ' || STRING_AGG(
                        DISTINCT p.phone || ' (' || p.type || ')',
                        ', '
                    )
                    ELSE ''
                END AS phones,
                c.created_at

            FROM contacts c

            LEFT JOIN groups g
                ON c.group_id = g.id

            LEFT JOIN phones p
                ON p.contact_name = c.username

            WHERE
                (%s = 'all' OR g.name ILIKE %s)
                AND (%s = '' OR COALESCE(c.email, '') ILIKE %s)

            GROUP BY
                c.username,
                c.email,
                c.birthday,
                g.name,
                c.phone,
                c.created_at

            ORDER BY """ + sort_column + """ NULLS LAST

            LIMIT %s OFFSET %s
        """

        with connect_db() as conn:
            with conn.cursor() as cur:

                cur.execute(
                    query,
                    (
                        group_name,
                        group_name,
                        email_query,
                        '%' + email_query + '%',
                        page_size,
                        offset
                    )
                )

                rows = cur.fetchall()

        if not rows:
            print("No contacts found on this page.")

            if page > 0:
                page -= 1

        else:

            print("\n===== CONTACTS =====")

            for row in rows:
                print("--------------------")
                print("Name:", row[0])
                print("Email:", row[1])
                print("Birthday:", row[2])
                print("Group:", row[3])
                print("Phones:", row[4])
                print("Date added:", row[5])

        print("\nCurrent page:", page + 1)

        command = input("Enter next / prev / quit: ").lower()

        if command == "next":
            page += 1

        elif command == "prev":

            if page > 0:
                page -= 1
            else:
                print("You are already on the first page.")

        elif command == "quit":
            break

        else:
            print("Invalid command!")


# Main menu
def main():

    while True:

        print("\n===== PHONEBOOK =====")
        print("1. Search contacts")
        print("2. Insert or update contact")
        print("3. Insert many contacts")
        print("4. Show contacts by pages")
        print("5. Delete contact")
        print("6. Advanced search and filter")
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

        elif choice == "6":

            advanced_search()

        elif choice == "0":

            print("Goodbye!")
            break

        else:

            print("Invalid choice!")


if __name__ == "__main__":
    main()
