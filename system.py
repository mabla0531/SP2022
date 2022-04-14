from tkinter import *
from tkinter import ttk
import os



root = Tk()
root.attributes('-fullscreen', True)
root.configure(bg='blue', cursor='none')

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

def log_new_image():
    print("log")
def scan_for_faces():
    print("scan")
def remove_image():
    print("remove")

Button(root, text="Log New Image", bg="blue", fg="white", command=log_new_image).place(x=1, y=1, width=WIDTH/2, height=HEIGHT/2)
Button(root, text="Begin Scanning", bg="blue", fg="white", command=scan_for_faces).place(x=WIDTH/2, y=1, width=WIDTH/2, height=HEIGHT/2)
Button(root, text="Remove Image", bg="blue", fg="white", command=remove_image).place(x=1, y=HEIGHT/2, width=WIDTH/2, height=HEIGHT/2)
Button(root, text="Exit", bg="blue", fg="white", command=root.destroy).place(x=WIDTH/2, y=HEIGHT/2, width=WIDTH/2, height=HEIGHT/2)

root.mainloop()