import tkinter as tk
from tkinter import *

r = tk.Tk() 
r.title('Upkeepmonitor') 
r.geometry("800x600")
r.configure(bg="blue")
r.iconbitmap("icon.ico")

networkname = tk.Canvas(r,width=300,height=50,bg="white")

networkname.place(relx=0.5,rely=0.1,anchor=CENTER)

rectangle1 = tk.Canvas(r, width=150,height=400, bg="white")
rectangle1.place(relx=0.1,rely=0.3)

r.mainloop() 












