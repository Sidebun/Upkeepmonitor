import Upkeepmonitoring as GUI
import tkinter as tk
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
        sleep(10)
        try:
            requests.get(host).ok
            print("You're Online")
            #onlinestatus=True
        except:
            print("You're Offline")
            #onlinestatus=False
    


def networkscan():
    from Upkeepmonitoring import listAddedHosts
    while True:
        global listHosts
        global listIps
        global current_hostsIP
        print("SCANNING")
        network='192.168.1.*'
        hostname = socket.gethostname()
        ownDeviceIP = socket.gethostbyname(hostname)
        nm = nmap.PortScanner()
        nm.scan(hosts=network,arguments='-sn')
        current_hostsIP = nm.all_hosts() # current_hostsIP alltid uppdaterad med om hosts försvinner eller inte
        for IP in current_hostsIP:
            if (IP != ownDeviceIP and IP not in listIps):
                if socket.gethostbyaddr(IP)[0] not in listHosts:
                    listHosts.append(socket.gethostbyaddr(IP)[0])
                    listIps.append(IP)
        
        for host in current_hostsIP:
            if host not in listAddedHosts:
                    GUI.listBoxAdd()
        
        loggingfunc()

        listHosts = []
        listIps = []




def loggingfunc():
    import dbUpkeepMonitor as db
    from Upkeepmonitoring import listAddedHosts
    for host in listAddedHosts:
        try:
            ipdb = socket.gethostbyname(host)
        except:
            print("Error finding IP of", host,)
        if host not in listHosts:
            hoststatus = "Not Reachable"
        elif host in listHosts:
            hoststatus = "Reachable"
        db.table_insert(host,ipdb,hoststatus)
            




def mainProgram():
    threadScan = threading.Thread(target=networkscan,daemon=True)
    threadScan.start()
    threadConnection = threading.Thread(target=connected,daemon=True)
    threadConnection.start()
    #t1 = threading.Thread(target=loggingfunc,daemon=True)
    #t1.start()
    GUI.TkGUI()