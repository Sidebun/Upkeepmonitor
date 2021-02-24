import Upkeepmonitoring as GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import threading
from threading import Thread
import nmap
import socket
from time import time, sleep

def oneplusone():
    print("1+1=2")



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


def networkscan():
    network='192.168.1.*'
    nm = nmap.PortScanner()
    nm.scan(hosts=network,arguments='-sn')
    for x in nm.all_hosts():
        print(socket.gethostbyaddr(x))

    print("All hosts found.")
    GUI.TkGUI()
    x = threading.Thread(target=connected,daemon=True)
    x.start()
        #connected()
        



