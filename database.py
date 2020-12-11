import sqlite3

CREATE_TABLE_contact = "CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY, name TEXT, number INTEGER,nickname TEXT);"

INSERT_contact = "INSERT INTO contact (name, number, nickname) VALUES (?, ?, ?);"

GET_contact_BY_NAME = "SELECT * FROM contact WHERE name = ?;"

GET_ALL_contact = "SELECT * FROM contact;"

GET_contact_BY_NUMBER = "SELECT * FROM contact WHERE number = ?;"

def connect():
    return sqlite3.connect("data.db")

def Create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_contact)

def add_contact(connection, name, number, nickname):
    with connection:
        connection.execute(INSERT_contact, (name, number, nickname))

def search_by_name(connection, name):
    with connection:
        return connection.execute(GET_contact_BY_NAME, (name,)).fetchall()

def get_all_contact(connection):
    with connection:
        return connection.execute(GET_ALL_contact).fetchall()

def search_by_number(connection, number):
    with connection:
        return connection.execute(GET_contact_BY_NUMBER,(number,))
