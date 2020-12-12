import database   # importing database.py(user defined) file for database interaction.
import tkinter as tk  #importing Tkinter for GUI.
from PIL import ImageTk, Image #importing PIL for rendering image.

# function that insert new contact.
def insert_contact():
    pass

# Function that search contact
def search_contact():
    pass

# Function that delete contact
def delete_contact():
    pass

# function that return rendered image.
def image_render(path):
    #function that render any image.
    image = Image.open(path) 
    randered_image = ImageTk.PhotoImage(image)
    return randered_image

def menu():  
    connection = database.connect()
    database.Create_tables(connection)
    
    wel_scr = tk.Tk() #making a tkinter object
    wel_scr.title("Contact Saver By D")  #title of application
    
    image = Image.open("Image\\BG.jpg")                            # Background Image for main window ----
    randered_image = ImageTk.PhotoImage(image)                                                            #
    bg_label = tk.Label(master=wel_scr, image = randered_image)   #--------------- End Here--------------
    
    w = image_render("Image\\BG.jpg").width()                      #taking the height and width of bg image for size of window                                                           
    h = image_render("Image\\BG.jpg").height()                                                                                #
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
        command = insert_contact
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
        command = search_contact
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
        command = delete_contact
        )
    # placing all the button in main window.
    delete_button.place(x = 23, y = 600)
    search_button.place(x = 23, y = 320)
    insert_button.place(x = 23, y = 80)
    bg_label.place(x = 0, y = 0)
    wel_scr.mainloop()   # mainloop always required.

#calling the main function
menu()