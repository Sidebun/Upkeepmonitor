import Upkeepmonitoring as GUI
import tkinter as tk
#from tkinter import *
from tkinter import messagebox
import requests
import threading
from threading import Thread
import nmap
import socket
from time import time, sleep
from datetime import datetime,date


listHosts = list()
listIps = list()
hoststatus = "N/A"
onlinestatus=False

def connected():
    host="http://google.com"
    while True:
        sleep(2)
        try:
            requests.get(host).ok
            print("You're Online")
            #onlinestatus=True
        except:
            print("You're Offline")
            #onlinestatus=False
    


def networkscan():
    from Upkeepmonitoring import listAdded
    while True:
        global listHosts
        global listIps
        sleep(2)
        print("Starting scan of network.")
        network='192.168.1.*'
        hostname = socket.gethostname()
        ownDeviceIP = socket.gethostbyname(hostname)
        nm = nmap.PortScanner()
        nm.scan(hosts=network,arguments='-sn')
        current_hosts = nm.all_hosts() # Current_hosts alltid uppdaterad med om hosts försvinner eller inte
        
        

        for IP in current_hosts:
            if (IP != ownDeviceIP and IP not in listIps):
                if socket.gethostbyaddr(IP)[0] not in listHosts:
                    listHosts.append(socket.gethostbyaddr(IP)[0]) #Denna#########
                listIps.append(IP)
        print(listHosts)
        print(listIps)
        print("All hosts found.")
        
        for host in current_hosts:
            if host not in listAdded:
                    GUI.listBoxAdd()
        listHosts = []
        listIps = []
        



def loggingfunc():
    #lägg till om reachable eller inte
    #uptime = hur länge det vart anslutet
    while True:
        sleep(5)
        for host in listHosts:
            print(datetime.now(), host)


def mainProgram():
    tn = threading.Thread(target=networkscan,daemon=True)
    tn.start()
    x = threading.Thread(target=connected,daemon=True)
    x.start()
    t1 = threading.Thread(target=loggingfunc,daemon=True)
    t1.start()
    GUI.TkGUI()