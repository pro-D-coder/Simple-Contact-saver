import database
import tkinter as tk
from PIL import ImageTk, Image

def menu():  
    connection = database.connect()
    database.Create_tables(connection)
    
    wel_scr = tk.Tk()

    wel_scr.title("Contact Saver By D")

    wel_scr.geometry("800x700")

    
    
   
    

    wel_scr.mainloop()

menu()