from tkinter import *
from tkinter import ttk
import os
import take_picture as pic

root = Tk()
root.attributes('-fullscreen', True)
root.configure(bg='blue', cursor='none')

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

def log_new_image():
    print("log")
    pic.picture(root_window=root)
def scan_for_faces():
    print("scan")

new_image = Button(root, text="Log New Image", bg="blue", fg="white", font=('Helvetica', '20'), command=log_new_image).place(x=1, y=1, width=WIDTH/2, height=HEIGHT/2)
scan = Button(root, text="Begin Scanning", bg="blue", fg="white", font=('Helvetica', '20'), command=scan_for_faces).place(x=WIDTH/2, y=1, width=WIDTH/2, height=HEIGHT/2)
image = Canvas(root).place(x=1, y=HEIGHT/2, width=WIDTH/2, height=HEIGHT/2)
exit_app = Button(root, text="Exit", bg="blue", fg="white", font=('Helvetica', '20'), command=root.destroy).place(x=WIDTH/2, y=HEIGHT/2, width=WIDTH/2, height=HEIGHT/2)

root.mainloop()
