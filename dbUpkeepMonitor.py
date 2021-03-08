import sqlite3
from sqlite3 import Error
import time
from datetime import datetime,date
import socket


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    global conn
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def table_insert(hostname,ip,hoststatus):
    timestamp = datetime.now()
    name = hostname
    ipaddress = ip
    status = hoststatus

    conn = create_connection("db.db")
    c = conn.cursor()
    print(hostname,ip,date,status)
#create table
    c.execute('''CREATE TABLE IF NOT EXISTS networklog
             (name text, ipaddress text, timestamp text, status text)''')

    c.execute("INSERT INTO networklog values (?,?,?,?)",
                (name,ipaddress,timestamp,status))
    
			 
#commit the changes to db			
    conn.commit()
#close the connection
    conn.close()

########table_insert("XD","192.168.1.1")

