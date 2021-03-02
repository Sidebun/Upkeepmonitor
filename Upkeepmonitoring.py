import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import threading
from threading import Thread
import nmap
import socket
from time import time, sleep
import upkeepfunctions as func


listAdded = list()
onlinestatus="N/A"



def TkGUI():
    from upkeepfunctions import listHosts,listIps
    global r
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

    global lD
    lD = Listbox(r)
    lD.configure(width=15,height=10,font=("MS Sans Serif",15))
    lD.place(relx=0.18,rely=0.60,anchor=CENTER)


    #------------------------------------------------------------------#
    #When it adds device it will also insert the IP for the device, (lIP.insert(DeviceNr,"IP"))
    global lIP
    lIP = Listbox(r)

    lIP.configure(width=45,height=10,font=("MS Sans Serif",15))
    lIP.place(relx=0.5,rely=0.60,anchor=CENTER)
    #------------------------------------------------------------------#
    global lStatus
    lStatus = Listbox(r)
    lStatus.configure(width=15,height=10,font=("MS Sans Serif",15))
    lStatus.place(relx=0.8,rely=0.60,anchor=CENTER)

    DeviceCanvas.place(relx=0.5,rely=0.6,anchor=CENTER)

    r.resizable(False, False)
    r.mainloop() 



def listBoxAdd():
    from upkeepfunctions import listHosts,listIps
    HostCount=1
    IpCount=1
    StatusCount=1
    for host in listHosts:
        if host not in listAdded:
                lD.insert(HostCount,host)
                HostCount+=1
                listAdded.append(host)
    for ip in listIps:
        if ip not in listAdded:
            lIP.insert(IpCount,ip)
            IpCount +=1
            listAdded.append(ip)
    lStatus.delete(0,END)
    for host in listHosts:
        if host in listHosts:
            lStatus.insert(StatusCount,"Reachable")

        else: #host in listAdded and host not in listHosts:
            lStatus.insert(StatusCount,"Not Reachable")


if __name__=="__main__":
    func.mainProgram()


list = [["ROUTER","IP","STATUS"],["TELEFON","IP","STATUS"]]