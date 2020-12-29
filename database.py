import sqlite3    #importing sqlite3 for database
from tkinter import messagebox #importing messagebox for showing info and error and warnings

#variable that store quary for creating a contact table
CREATE_TABLE_contact = "CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY, name TEXT, number TEXT,nickname TEXT);"
#variable that store quary for selecting only name column from contact table
SELECT_NAME = "SELECT name FROM contact"
#variable that store quary for inserting a contact in contact table
INSERT_contact = "INSERT INTO contact (name, number, nickname) VALUES (?, ?, ?);"
#variable that store quary for getting info using name from contact table
GET_contact_BY_NAME = "SELECT * FROM contact WHERE name = ?;"
#variable that store quary for getting info using nickname from contact table
GET_contact_BY_NICKNAME = "SELECT * FROM contact WHERE nickname = ?;"
#variable that store quary for getting info using number from contact table
GET_contact_BY_NUMBER = "SELECT * FROM contact WHERE number = ?;"
#variable that store quary for deleting info using name from contact table
DELETE_BY_NAME = "DELETE FROM contact WHERE name = ?;"
#variable that store quary for deleting info using number from contact table
DELETE_BY_NUMBER = "DELETE FROM contact WHERE number = ?;"
#variable that store quary for deleting info using nickname from contact table
DELETE_BY_NICKNAME = "DELETE FROM contact WHERE nickname = ?;"
#variable that store quary for searching recommandation info from contact
GET_contact_BY_NAME_RE = "SELECT name FROM contact WHERE name LIKE ? || '%';"
#variable that store quary for searching recommandation info from contact
GET_contact_BY_NUMBER_RE = "SELECT number FROM contact WHERE number LIKE ? || '%';"
#variable that store quary for searching recommandation info from contact
GET_contact_BY_NICKNAME_RE = "SELECT nickname FROM contact WHERE nickname LIKE ? || '%';"
# Function that return connection between database
def connect():
    return sqlite3.connect("data.db")

#function that create contact table
def Create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_contact)

#function that add contact into database
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
                messagebox.showinfo("Insert Window","Contact inserted !")
                cur.close()
#def get_all_contact(connection):
#    with connection:
#        return connection.execute(GET_ALL_contact).fetchall()

# Function that search for info in database
def search_by_choice(connection, entry, check_by):
    try: 
        if(check_by == "name"):
            with connection:
                cur = connection.cursor()
                search_result = cur.execute(GET_contact_BY_NAME, (entry,)).fetchone()
                if search_result != None:
                    messagebox.showinfo("Contact Information","Name: "+ str(search_result[1]) +"\nNumber: " + str(search_result[2]) + "\nNickname: " + str(search_result[3]))
                else:
                    messagebox.showerror("No contact","Name Not Exist!!")
        elif(check_by == "nickname"):
            cur = connection.cursor()
            search_result = cur.execute(GET_contact_BY_NICKNAME, (entry,)).fetchone()
            if search_result != None:
                messagebox.showinfo("Contact Information","Name: "+ str(search_result[1]) +"\nNumber: " + str(search_result[2]) + "\nNickname: " + str(search_result[3]))
            else:
                messagebox.showerror("No contact","Nickname Not Exist!!")
        else:
            with connection:
                cur = connection.cursor()
                search_result = cur.execute(GET_contact_BY_NUMBER, (entry,)).fetchone()
                if search_result != None:
                    messagebox.showinfo("Contact Information","Name: "+ str(search_result[1]) +"\nNumber: " + str(search_result[2]) + "\nNickname: " + str(search_result[3]))
                else:
                    messagebox.showerror("No contact","Number Not Exist!!")
    except Exception as e:
        messagebox.showerror("Error",entry)

# Function that delete info from database
def delete_by_choice(connection,entry,delete_by): 
    try:    
        if(delete_by == "name"):
            with connection:
                cur = connection.cursor()
                search_result = cur.execute(GET_contact_BY_NAME, (entry,)).fetchone()
                if search_result != None:
                    ask = messagebox.askquestion("Warning","Do You Really Want To Insert!")
                    if ask == 'yes':
                        messagebox.showinfo("Delete Window","Contact deleted with:\nName: "+ str(search_result[1]) +"\nNumber: " + str(search_result[2]) + "\nNickname: " + str(search_result[3]))
                        connection.execute(DELETE_BY_NAME, (entry, ))
                else:
                    messagebox.showerror("No contact","Name Not Exist!!")   
        elif(delete_by == "nickname"):
            with connection:
                cur = connection.cursor()
                search_result = cur.execute(GET_contact_BY_NICKNAME, (entry,)).fetchone()
                if search_result != None:
                    ask = messagebox.askquestion("Warning","Do You Really Want To Insert!")
                    if ask == 'yes':
                        messagebox.showinfo("Delete window","Contact deleted with:\nName: "+ str(search_result[1]) +"\nNumber: " + str(search_result[2]) + "\nNickname: " + str(search_result[3]))
                        connection.execute(DELETE_BY_NICKNAME, (entry, ))
                else:
                   messagebox.showerror("No contact","Nickname Not Exist!!")
        else:
            with connection:
                cur = connection.cursor()
                search_result = cur.execute(GET_contact_BY_NUMBER, (entry,)).fetchone()
                if search_result != None:
                    ask = messagebox.askquestion("Warning","Do You Really Want To Insert!")
                    if ask == 'yes':
                        messagebox.showinfo("Delete Window","Contact deleted with:\nName: "+ str(search_result[1]) +"\nNumber: " + str(search_result[2]) + "\nNickname: " + str(search_result[3]))
                        connection.execute(DELETE_BY_NUMBER, (entry, ))
                else:
                    messagebox.showerror("No contact","Number Not Exist!!")
    except Exception as e:
        messagebox.showerror("Error",entry)

#Function that return recommandation list of tuple
def search_recom(connection,name,check_by):
    with connection:
        cur = connection.cursor()
        if str(check_by.get()) == "name":
            search_result = cur.execute(GET_contact_BY_NAME_RE, (name,)).fetchall()
            return search_result
        elif str(check_by.get()) == "number":
            search_result = cur.execute(GET_contact_BY_NUMBER_RE, (name,)).fetchall()
            return search_result
        else:
            search_result = cur.execute(GET_contact_BY_NICKNAME_RE, (name,)).fetchall()
            return search_result