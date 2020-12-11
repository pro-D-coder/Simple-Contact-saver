import database

def menu():  
    connection = database.connect()
    database.Create_tables(connection)
