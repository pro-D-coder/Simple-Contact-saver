import sqlite3

CREATE_TABLE_CONTECT = "CREATE TABLE IF NOT EXISTS contect (id INTEGER PRIMARY KEY, name TEXT, number INTEGER,nickname TEXT);"

INSERT_CONTECT = "INSERT INTO contect (name, number, nickname) VALUES (?, ?, ?);"

GET_CONTECT_BY_NAME = "SELECT * FROM contect WHERE name = ?;"

GET_ALL_CONTECT = "SELECT * FROM contect;"

GET_CONTECT_BY_NUMBER = "SELECT * FROM contect WHERE number = ?;"

def connect():
    return sqlite3.connect("data.db")

def Create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_CONTECT)

def add_contect(connection, name, number, nickname):
    with connection:
        connection.execute(INSERT_CONTECT, (name, number, nickname))

def search_by_name(connection, name):
    with connection:
        return connection.execute(GET_CONTECT_BY_NAME, (name,)).fetchall()

def get_all_contact(connection):
    with connection:
        return connection.execute(GET_ALL_CONTECT).fetchall()

def search_by_number(connection, number):
    with connection:
        return connection.execute(GET_CONTECT_BY_NUMBER,(number,))
