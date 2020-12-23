import sqlite3
from tkinter import messagebox

CREATE_TABLE_contact = "CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY, name TEXT, number TEXT,nickname TEXT);"

SELECT_NAME = "SELECT name FROM contact"

INSERT_contact = "INSERT INTO contact (name, number, nickname) VALUES (?, ?, ?);"

GET_contact_BY_NAME = "SELECT * FROM contact WHERE name = ?;"

GET_ALL_contact = "SELECT * FROM contact;"

GET_contact_BY_NUMBER = "SELECT * FROM contact WHERE number = ?;"

DELETE_BY_NAME = "DELETE FROM contact WHERE name = ?;"

DELETE_BY_NUMBER = "DELETE FROM contact WHERE number = ?;"

def connect():
    return sqlite3.connect("data.db")

def Create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_contact)

def add_contact(connection, name, number, nickname):
    with connection:
        cur = connection.cursor()
        check = False
        all_name = connection.execute(SELECT_NAME).fetchall()
        for i in range(0, len(all_name)):
                if(all_name[i][0] == name):
                    check = True
                    messagebox.showerror("Name Error", "Name Already Exist!!")
                    break  
        if check != True:
            ask = messagebox.askquestion("Warning","Do You Really Want To Insert!")
            if ask == 'yes':
                cur.execute(INSERT_contact, (name, number, nickname))
                cur.close()
def get_all_contact(connection):
    with connection:
        return connection.execute(GET_ALL_contact).fetchall()

def search_by_choice(connection, entry, check_by):
    if(check_by == "name"):
        with connection:
            cur = connection.cursor()
            search_result = cur.execute(GET_contact_BY_NAME, (entry,)).fetchone()
            if search_result != None:
                messagebox.showinfo("Contact Information","Name: "+ str(search_result[1]) +"\nNumber: " + str(search_result[2]) + "\nNickname: " + str(search_result[3]))
            else:
                messagebox.showerror("No contact","Name Not Exist!!")
    else:
        with connection:
            cur = connection.cursor()
            search_result = cur.execute(GET_contact_BY_NUMBER, (entry,)).fetchone()
            if search_result != None:
                messagebox.showinfo("Contact Information","Name: "+ str(search_result[1]) +"\nNumber: " + str(search_result[2]) + "\nNickname: " + str(search_result[3]))
            else:
                messagebox.showerror("No contact","Number Not Exist!!")

def delete_by_name(connection, name):
    with connection:
        connection.execute(DELETE_BY_NAME, (name, ))

def delete_by_number(connection, number):
    with connection:
        connection.execute(DELETE_BY_NUMBER, (number, ))