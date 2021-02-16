import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import threading
from threading import Thread
import nmap
import socket
from time import time, sleep



onlinestatus="N/A"


def TkGUI():
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
    #------------------------------------------------------------------#
    #Devices will be shown here with all information for it.
    DeviceCanvas = tk.Canvas(r, width=1000,height=650, bg="#626262")

    #------------------------------------------------------------------#
    button1 = Button(r, text = "Devices",command=r.quit, anchor = W,bg="white")
    button1.configure(width =12,font=("MS Sans Serif",20),relief=RAISED,borderwidth=5)
    button1_window = DeviceCanvas.create_window(1, 0, anchor=NW, window=button1)

    #------------------------------------------------------------------#
    button2 = Button(r, text = "IP Address", anchor = W,bg="white")
    button2.configure(width =12,font=("MS Sans Serif",20),relief=RAISED,borderwidth=5)
    button2_window = DeviceCanvas.create_window(300, 0, anchor=NW, window=button2)
    #------------------------------------------------------------------#
    button3 = Button(r, text = "Status", anchor = W,bg="white")
    button3.configure(width =10,font=("MS Sans Serif",20),relief=RAISED,borderwidth=5)
    button3_window = DeviceCanvas.create_window(800, 0, anchor=NW, window=button3)
    #------------------------------------------------------------------#
    #List Devices, Should be able to add dynamically with  lD.insert(DeviceNr,"NameOfDevice") or something like that.
    lD = Listbox(r)
    lD.insert(1,"Soren PC")
    lD.insert(2,"Duh")
    lD.insert(3,"Soren dsadsadsadsdsadPC")
    lD.insert(4,"Soren PC")

    lD.configure(width=15,height=20,font=("MS Sans Serif",15))
    lD.place(relx=0.18,rely=0.60,anchor=CENTER)

    #------------------------------------------------------------------#
    #When it adds device it will also insert the IP for the device, (lIP.insert(DeviceNr,"IP"))
    lIP = Listbox(r)

    lIP.insert(1,"192.168.0.1")
    lIP.insert(2,"192.168.1.1")
    lIP.insert(3,"127.0.0.1")
    lIP.insert(4,"10.0.0.1")

    lIP.configure(width=45,height=20,font=("MS Sans Serif",15))
    lIP.place(relx=0.5,rely=0.60,anchor=CENTER)
    #------------------------------------------------------------------#

    lStatus = Listbox(r)
    if (onlinestatus==True):
        lStatus.insert(1,"UP")
    else:
        lStatus.insert(1,"DOWN")


    



    lStatus.configure(width=15,height=20,font=("MS Sans Serif",15))
    lStatus.place(relx=0.8,rely=0.60,anchor=CENTER)

    DeviceCanvas.place(relx=0.5,rely=0.6,anchor=CENTER)

    r.resizable(False, False)







    r.mainloop() 


class Network(object):
    def __init__(self):
        ip="192.168.1.1"
        self.ip = ip

    def networkscanner(self):
        if len(self.ip) == 0:
            network = '192.168.1.1/24'
        else:
            network = self.ip +'/24'
        
        print("Scanning please wait ----->")

        nm = nmap.PortScanner()
        nm.scan(hosts=network,arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print(socket.gethostbyaddr("192.168.1.90"))
            print("Host\t{}".format(host))

        TkGUI()



if __name__=="__main__":
    D = Network()
    D.networkscanner()




#probably implement this into network scan for scan & onlinecheck every n seconds.
def connected():
    host="http://google.com"
    if requests.get(host).ok:
        print("You're Online")
        onlinestatus=True
    else:
        print("You're Offline")
        onlinestatus=False
    while True:
        sleep(1 - time() % 1)
        connected()

x = threading.Thread(target=connected,daemon=True)
x.start()