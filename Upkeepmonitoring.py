import tkinter as tk
from tkinter import *

r = tk.Tk() 
r.title('Upkeepmonitor') 
r.geometry("1280x960")
r.configure(bg="#023562")
r.iconbitmap("icon.ico")
NameOfNetwork="NETWORKNAME"
#Width and height to be adjusted based on networkname that the program finds
networkname = tk.Text(r,width=len(NameOfNetwork),height=1,fg="white",bg="#626262")
networkname.config(font=("Courier",30)) #Set font & size of text.
networkname.place(relx=0.5,rely=0.1,anchor=CENTER) #Set position relative to screen.
networkname.insert(tk.END,NameOfNetwork) #Insert the text "NameOfNetwork"

networkname.config(state='disabled') #Disable input/editing of networkname text.
#-------------------------------------------------------------------------------------------------#

#NameBarForDevices = tk.Text(r,width=62,height=1,bg="blue",fg="white")
#NameBarForDevices.config(font=("Courier",20)) #Set font & size of text
#NameBarForDevices.place(relx=0.5,rely=0.21,anchor=CENTER)

#Devices will be shown here with all information for it.
DeviceCanvas = tk.Canvas(r, width=1000,height=650, bg="#626262")


button1 = Button(r, text = "Devices", anchor = W,bg="white")
button1.configure(width =10,font=("MS Sans Serif",20),relief=RAISED,borderwidth=5)
button1_window = DeviceCanvas.create_window(0, 0, anchor=NW, window=button1)


button2 = Button(r, text = "IP Address", anchor = W,bg="white")
button2.configure(width =10,font=("MS Sans Serif",20),relief=RAISED,borderwidth=5)
button2_window = DeviceCanvas.create_window(250, 0, anchor=NW, window=button2)

button3 = Button(r, text = "Status", anchor = W,bg="white")
button3.configure(width =10,font=("MS Sans Serif",20),relief=RAISED,borderwidth=5)
button3_window = DeviceCanvas.create_window(800, 0, anchor=NW, window=button3)




DeviceCanvas.place(relx=0.5,rely=0.6,anchor=CENTER)


r.resizable(False, False) 
r.mainloop() 












