import Upkeepmonitoring as GUI
import tkinter as tk
from tkinter import messagebox, simpledialog
import requests
import threading
from threading import Thread
import nmap
import socket
from time import time, sleep
from datetime import datetime,date
#from pythonping import ping
from getmac import get_mac_address
import subprocess

listHostsMacs = list()
listHosts = list()
listIps = list()
hoststatus = "N/A"



def connected():
    from Upkeepmonitoring import networkStatusBox
    global onlinestatus
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        print("ONLINE")
        networkStatusBox(True)
        onlinestatus = True               
    except subprocess.CalledProcessError:
        print("OFFLINE")
        networkStatusBox(False)
        onlinestatus = False
            

def networkscan():
    from Upkeepmonitoring import listAddedHosts
    global USER_INP
    root = tk.Tk()
    root.withdraw()
    # the input dialog
    USER_INP = simpledialog.askstring(title="Upkeepmonitor",
                                    prompt="What's your default gateway? Example : 192.168.1.1")

    if USER_INP == "" or USER_INP == None:
        sleep(3)
        networkscan()

    while USER_INP != "" and USER_INP != None:
        global listHosts
        global listIps
        global current_hostsIP
        USER_INP = USER_INP[:-1] + "*"
        networkGateway = USER_INP
        sleep(1)
        connected()
        print("SCANNING")
        network=networkGateway
        hostname = socket.gethostname()
        ownDeviceIP = socket.gethostbyname(hostname)
        nm = nmap.PortScanner()
        nm.scan(hosts=network,arguments='-sn')
        current_hostsIP = nm.all_hosts() # current_hostsIP alltid uppdaterad med om hosts försvinner eller inte



        for IP in current_hostsIP:
            if (IP != ownDeviceIP and IP not in listIps):
                try:
                    if onlinestatus == True:
                        if socket.gethostbyaddr(IP)[0] not in listHosts:
                                listHosts.append(socket.gethostbyaddr(IP)[0])
                                listIps.append(IP)
                    elif onlinestatus == False:
                        if get_mac_address(ip=IP) not in listHostsMacs:
                                listHostsMacs.append(get_mac_address(ip=IP))
                                listIps.append(IP)
                except:
                    print("Error occured retrieving hostname from", IP)

        for host in listHosts:
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
    #threadConnection = threading.Thread(target=connected,daemon=True)
    #threadConnection.start()
    GUI.TkGUI()