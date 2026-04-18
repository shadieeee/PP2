import csv, psycopg2
from connect import connect

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS contacts (id SERIAL PRIMARY KEY, name TEXT, phone TEXT);")
    conn.commit()

def insert_csv(conn, file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        with conn.cursor() as cur:
            for r in reader:
                cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (r[0], r[1]))
    conn.commit()

def insert_user(conn):
    data = (input("Name: "), input("Phone: "))
    with conn.cursor() as cur:
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", data)
    conn.commit()

def find_contact(conn):
    val = input("Search: ")
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s OR phone LIKE %s", (f'%{val}%', f'{val}%'))
        for r in cur.fetchall(): print(r)

def delete_contact(conn):
    val = input("Delete (name/phone): ")
    with conn.cursor() as cur:
        cur.execute("DELETE FROM contacts WHERE name = %s OR phone = %s", (val, val))
    conn.commit()

if __name__ == '__main__':
    conn = connect()
    if conn:
        create_table(conn)
        actions = {'1': lambda: insert_csv(conn, 'contacts.csv'), '2': lambda: insert_user(conn), 
                   '3': lambda: find_contact(conn), '4': lambda: delete_contact(conn)}
        while True:
            print("\n1:CSV 2:Add 3:Find 4:Del 0:Exit")
            cmd = input("> ")
            if cmd == '0': break
            if cmd in actions: actions[cmd]()
        conn.close()