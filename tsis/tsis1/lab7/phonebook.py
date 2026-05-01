from importlib.resources import path

from connect import get_connection
import csv
import json
import os


def validate_phone_type(t):
    return t if t in ("home", "work", "mobile") else "mobile"


class PhoneBook:

    def add_extended_contact(self):
        name = input("Name: ").strip()
        email = input("Email: ").strip() or None
        birthday = input("Birthday (YYYY-MM-DD): ").strip() or None
        group_name = input("Group: ").strip()

        phone = input("Phone: ").strip()
        p_type = validate_phone_type(input("Type: ").strip().lower())

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id FROM groups WHERE name=%s", (group_name,))
        g = cur.fetchone()

        if g:
            gid = g[0]
        else:
            cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group_name,))
            gid = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO contacts(first_name, phone, email, birthday, group_id)
            VALUES (%s,%s,%s,%s,%s)
            RETURNING id
        """, (name, phone, email, birthday, gid))

        cid = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO phones(contact_id, phone, type) VALUES (%s,%s,%s)",
            (cid, phone, p_type)
        )

        conn.commit()
        cur.close()
        conn.close()

    # ---------------- ADD PHONE ----------------
    def add_phone(self):
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        p_type = validate_phone_type(input("Type: ").strip().lower())

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, p_type))

        conn.commit()
        cur.close()
        conn.close()

    # ---------------- MOVE GROUP ----------------
    def move_to_group(self):
        name = input("Name: ").strip()
        group = input("Group: ").strip()

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("CALL move_to_group(%s,%s)", (name, group))

        conn.commit()
        cur.close()
        conn.close()

    # ---------------- SHOW ----------------
    def show_all_contacts(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.id, c.first_name, c.phone, c.email, g.name
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            ORDER BY c.id
        """)

        for r in cur.fetchall():
            print(r)

        cur.close()
        conn.close()

    def show_full_contacts(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.first_name, c.email, g.name, p.phone, p.type
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON p.contact_id = c.id
        """)

        for r in cur.fetchall():
            print(r)

        cur.close()
        conn.close()

    def filter_by_group(self):
        group = input("Group: ").strip()

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.first_name, c.email
            FROM contacts c
            JOIN groups g ON c.group_id = g.id
            WHERE g.name=%s
        """, (group,))

        for r in cur.fetchall():
            print(r)

        cur.close()
        conn.close()

    # ---------------- SEARCH ----------------
    def search_by_email(self):
        txt = input("Email: ").strip()

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT first_name, email
            FROM contacts
            WHERE COALESCE(email,'') ILIKE %s
        """, ("%" + txt + "%",))

        for r in cur.fetchall():
            print(r)

        cur.close()
        conn.close()

    def search_all_fields(self):
        txt = input("Search: ").strip()

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM search_contacts(%s::text)", (txt,))
        for r in cur.fetchall():
            print(r)

        cur.close()
        conn.close()

    # ---------------- SORT ----------------
    def sort_contacts(self):
        print("1-name 2-birthday 3-date")
        c = input("Choose: ")

        order = {
            "1": "c.first_name",
            "2": "c.birthday",
            "3": "c.created_at"
        }.get(c)

        if not order:
            return

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f"""
            SELECT c.first_name, c.email, c.birthday
            FROM contacts c
            ORDER BY {order} NULLS LAST
        """)

        for r in cur.fetchall():
            print(r)

        cur.close()
        conn.close()

    
    def paginated_navigation(self):
        limit = int(input("Page size: "))

        conn = get_connection()
        cur = conn.cursor()

        offset = 0

        while True:
            cur.execute("""
                SELECT first_name, email
                FROM contacts
                ORDER BY id
                LIMIT %s OFFSET %s
            """, (limit, offset))

            rows = cur.fetchall()

            for r in rows:
                print(r)

            cmd = input("next / prev / quit: ")

            if cmd == "next":
                offset += limit
            elif cmd == "prev":
                offset = max(0, offset - limit)
            else:
                break

        cur.close()
        conn.close()

    def export_to_json(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.id, c.first_name, c.phone, c.email, g.name
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
        """)

        data = []

        for c in cur.fetchall():
            cid = c[0]

            cur.execute("SELECT phone, type FROM phones WHERE contact_id=%s", (cid,))
            phones = [{"phone": p[0], "type": p[1]} for p in cur.fetchall()]

            data.append({
                "name": c[1],
                "main_phone": c[2],
                "email": c[3],
                "group": c[4],
                "phones": phones
            })

        path = os.path.join(os.path.dirname(__file__), "contacts.json")

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        cur.close()
        conn.close()


    def import_from_json(self):
        path = os.path.join(os.path.dirname(__file__), "contacts.json")

        with open(path, encoding="utf-8") as f:
            data = json.load(f)

            conn = get_connection()
        cur = conn.cursor()

        for c in data:
            name = c["name"]
            email = c.get("email")
            group = c.get("group")

            if not group:
                group = "Other"

            cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
            g = cur.fetchone()

            if g:
                gid = g[0]
            else:
                cur.execute(
                    "INSERT INTO groups(name) VALUES (%s) RETURNING id",
                    (group,)
                )
                gid = cur.fetchone()[0]

            cur.execute("SELECT id FROM contacts WHERE first_name=%s", (name,))
            exists = cur.fetchone()

            if exists:
                cid = exists[0]

                cur.execute("""
                    UPDATE contacts
                    SET phone=%s,
                        email=%s,
                        group_id=%s
                    WHERE id=%s
                """, (c.get("main_phone"), email, gid, cid))

                cur.execute("DELETE FROM phones WHERE contact_id=%s", (cid,))

            else:
                cur.execute("""
                    INSERT INTO contacts(first_name, phone, email, group_id)
                    VALUES (%s,%s,%s,%s)
                    RETURNING id
                """, (name, c.get("main_phone"), email, gid))

                cid = cur.fetchone()[0]

            for p in c.get("phones", []):
                cur.execute("""
                    INSERT INTO phones(contact_id, phone, type)
                    VALUES (%s,%s,%s)
                """, (cid, p["phone"], p["type"]))

        conn.commit()
        cur.close()
        conn.close()
    def import_csv_extended(self):
        path = os.path.join(os.path.dirname(__file__), "contacts.csv")

        conn = get_connection()
        cur = conn.cursor()

        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for r in reader:
                name = r["name"]
                email = r["email"] or None
                birthday = r["birthday"] or None
                group = r["group"]

                phone = r["phone"]
                p_type = validate_phone_type(r["phone_type"].lower())

                cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
                g = cur.fetchone()

                if g:
                    gid = g[0]
                else:
                    cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group,))
                    gid = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO contacts(first_name, phone, email, birthday, group_id)
                    VALUES (%s,%s,%s,%s,%s)
                    RETURNING id
                """, (name, phone, email, birthday, gid))

                cid = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO phones(contact_id, phone, type)
                    VALUES (%s,%s,%s)
                """, (cid, phone, p_type))

        conn.commit()
        cur.close()
        conn.close()

    def menu(self):
        while True:
            print("\n1 Add 2 AddPhone 3 Move 4 Show 5 Full 6 Filter 7 Email 8 Search 9 Sort 10 Pages 11 Export 12 Import 13 CSV 0 Exit")
            c = input("Choose: ")

            if c == "1":
                self.add_extended_contact()
            elif c == "2":
                self.add_phone()
            elif c == "3":
                self.move_to_group()
            elif c == "4":
                self.show_all_contacts()
            elif c == "5":
                self.show_full_contacts()
            elif c == "6":
                self.filter_by_group()
            elif c == "7":
                self.search_by_email()
            elif c == "8":
                self.search_all_fields()
            elif c == "9":
                self.sort_contacts()
            elif c == "10":
                self.paginated_navigation()
            elif c == "11":
                self.export_to_json()
            elif c == "12":
                self.import_from_json()
            elif c == "13":
                self.import_csv_extended()
            elif c == "0":
                break


app = PhoneBook()
app.menu()