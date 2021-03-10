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
from getmac import get_mac_address
import subprocess
import csv
from csv import reader

listHostsMacs = list()
listHosts = list()
listIps = list()
hoststatus = "N/A"

def mainProgram():
    ROOT = tk.Tk()
    ROOT.withdraw()
    USER_INP = simpledialog.askstring(title="Upkeepmonitor",prompt="What's your default gateway? Example : 192.168.1.1")
    USER_INP = USER_INP[:-1] + "*"
    global networkGateway
    networkGateway = USER_INP

    threadScan = threading.Thread(target=networkscan,daemon=True)
    threadScan.start()
    if USER_INP != "" and USER_INP != None:
        GUI.TkGUI()
    else:
        mainProgram()

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
    global listHosts
    global listIps
    global current_hostsIP
    while True:
        sleep(5)
        connected()
        print("SCANNING")
        network=networkGateway
        hostname = socket.gethostname()
        ownDeviceIP = socket.gethostbyname(hostname)
        nm = nmap.PortScanner()
        nm.scan(hosts=network,arguments='-sn')
        current_hostsIP = nm.all_hosts()



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
            ipdb = "Unknown"
            print("Error finding IP of", host,)
        if host not in listHosts:
            hoststatus = "Not Reachable"
        elif host in listHosts:
            hoststatus = "Reachable"
        db.table_insert(host,ipdb,hoststatus)
        exportCSV(host,ipdb,hoststatus)
            


def exportCSV(hostname,ip,hoststatus):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    columns = ['Host','IP','Status','Timestamp']
    with open ('UpkeepCSV.csv','a') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if checkifcolneeded() == True:
            writer.writerow(columns)
        writer.writerow([hostname,ip,hoststatus,current_time])


def checkifcolneeded():
    with open("UpkeepCSV.csv",'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                print(row)
                if any ("Host" in row for row in csv_reader):
                    return False
                else:
                    return True
    read_obj.close()

