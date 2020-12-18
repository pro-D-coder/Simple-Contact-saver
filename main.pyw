import database   # importing database.py(user defined) file for database interaction.
import tkinter as tk  #importing Tkinter for GUI.
from PIL import ImageTk, Image #importing PIL for rendering image.

#making connection for database
connection = database.connect()
database.Create_tables(connection)

# function that return rendered image.
def image_render(path):
    image = Image.open(path) 
    randered_image = ImageTk.PhotoImage(image)
    return randered_image

# function that insert new contact.
def insert_window():
    wel_scr.destroy()  #closing the first window
    global insert_win
    insert_win = tk.Tk() #making a tkinter object
    insert_win.title("INSERT CONTACT")  #title of window
    
    image = Image.open("insert_bg.jpg")                # Background Image for main window ----
    randered_image = ImageTk.PhotoImage(image)                                                      #
    bg_label = tk.Label(insert_win, image = randered_image)   #--------------- End Here--------------
    
    w = image_render("insert_bg.jpg").width()           #taking the height and width of bg image for size of window                                                           
    h = image_render("insert_bg.jpg").height()                                                                    #
    insert_win.geometry('%dx%d+0+0' % (w,h))                             # setting the size of window equal to bg image size)
    
    name =  tk.StringVar()  #variable for storing name passed from name entry
    number =  tk.StringVar() #variable for storing number passed from number entry
    nickname = tk.StringVar() #variable for storing nickname passed from nickname entry
    #Entry and Label for name .
    name_entry = tk.Entry(
        insert_win,
        font = ("Arial", 12,"bold"),
        bd = 0, 
        bg = "#1c1c1a",
        width = 27,
        fg = "white",
        textvariable = name)
    name_label = tk.Label(
        insert_win, 
        text = "NAME :", 
        bg = "white", 
        font = ("Times new roman", 15),)
    
    #Entry and Label for Number
    number_entry = tk.Entry(
        insert_win,
        font = ("Arial", 12,"bold"),
        bd = 0, 
        bg = "#1c1c1a",
        width = 10,
        fg = "white",
        textvariable = number)
    number_label = tk.Label(
        insert_win, 
        text = "NUMBER :", 
        bg = "white", 
        font = ("Times new roman", 15),)
    
    #Entry and Label for Nickname
    nickname_entry = tk.Entry(
        insert_win,
        font = ("Arial", 12,"bold"),
        bd = 0, 
        bg = "#1c1c1a",
        width = 10,
        fg = "white",
        textvariable = nickname)
    nickname_label = tk.Label(
        insert_win, 
        text = "NICKNAME :", 
        bg = "white", 
        font = ("Times new roman", 15),)
    #insert button for appending data in database
    button_image = Image.open("insert.png")
    r_button_image = ImageTk.PhotoImage(button_image)
    insert_button = tk.Button(insert_win,
        image = r_button_image,
        relief = tk.FLAT,
        bd = 0, 
        command = lambda:database.add_contact(connection, name.get(), number.get(), nickname.get()), #passing values to addcontact function
        )

    insert_button.place(x = 410, y = 370,height = 70, width = 160)
    nickname_entry.place(x = 440, y = 230,height = 30,width = 200)
    nickname_label.place(x = 299, y = 230)
    number_label.place(x = 299, y = 140)
    number_entry.place(x = 400, y = 140,height = 30,width = 240)
    name_label.place(x = 300, y = 60)
    name_entry.place(x = 395, y = 60,height = 30)
    bg_label.place(x = 0, y = 0)
    insert_win.mainloop()

# Function that search contact
def search_window():
    pass

# Function that delete contact
def delete_window():
    pass


def menu():  
    global wel_scr
    wel_scr = tk.Tk() #making a tkinter object
    wel_scr.title("Contact Saver By D")  #title of application
    
    image = Image.open("BG.jpg")                            # Background Image for main window ----
    randered_image = ImageTk.PhotoImage(image)                                                            #
    bg_label = tk.Label(master=wel_scr, image = randered_image)   #--------------- End Here--------------
    
    w = image_render("BG.jpg").width()                      #taking the height and width of bg image for size of window                                                           
    h = image_render("BG.jpg").height()                                                                                #
    wel_scr.geometry('%dx%d+0+0' % (w,h))                          # setting the size of window equal to bg image size
    wel_scr.minsize(655,784)
    wel_scr.maxsize(655,784)

    # Button for inserting contact
    insert_button = tk.Button(
        wel_scr,
        text = "INSERT NEW CONTACT", 
        bg = "black",
        fg = "white",
        padx = 20,
        pady = 20,
        font = ("Arial", 12, "bold"),
        command = insert_window
        )
    
    # Button for searching contact
    search_button = tk.Button(
        wel_scr,
        text = "SEARCH CONTACT", 
        bg = "black",
        fg = "white",
        padx = 36.5,
        pady = 20,
        font = ("Arial", 12, "bold"),
        command = search_window
        )
    
    # Button for deleting contact 
    delete_button = tk.Button(
        wel_scr,
        text = "DELETE CONTACT", 
        bg = "black",
        fg = "white",
        padx = 36.5,
        pady = 20,
        font = ("Arial", 12, "bold"),
        command = delete_window
        )
    # placing all the button in main window.
    delete_button.place(x = 23, y = 600)
    search_button.place(x = 23, y = 320)
    insert_button.place(x = 23, y = 80)
    bg_label.place(x = 0, y = 0)
    wel_scr.mainloop()   # mainloop always required.

#calling the main function
menu()