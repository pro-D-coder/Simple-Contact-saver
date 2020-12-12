import database
import tkinter as tk
from PIL import ImageTk, Image



def image_render(path):
    #function that render any image.
    image = Image.open(path) 
    randered_image = ImageTk.PhotoImage(image)
    return randered_image
def menu():  
    connection = database.connect()
    database.Create_tables(connection)
    
    wel_scr = tk.Tk()
    wel_scr.title("Contact Saver By D")
    image = Image.open("Image\\BG.jpg")                            # Background Image for main window ----
    randered_image = ImageTk.PhotoImage(image)                                                            #
    bg_label = tk.Label(master=wel_scr, image = randered_image)    #--------------- End Here--------------
    w = image_render("Image\\BG.jpg").width()                                                             
    h = image_render("Image\\BG.jpg").height()
    wel_scr.geometry('%dx%d+0+0' % (w,h))
    wel_scr.minsize(655,784)
    wel_scr.maxsize(655,784)

    #
    insert_button = tk.Button(
        wel_scr,
        text = "INSERT NEW CONTACT", 
        bg = "black",
        fg = "white",
        padx = 20,
        pady = 20,
        font = ("Arial", 12, "bold"))
    insert_button.place(x = 23, y = 80)
    bg_label.place(x = 0, y = 0)
    wel_scr.mainloop()

menu()