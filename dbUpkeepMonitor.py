import sqlite3
from sqlite3 import Error
import time
from datetime import datetime,date


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    global conn
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def table_insert(hostname,ip):
    date = datetime.now()
    conn = create_connection("db.db")
    c = conn.cursor()

#create table
    c.execute('''CREATE TABLE IF NOT EXISTS networklog
             ( name text, ipaddress text, date text)''')

    c.execute('''INSERT INTO networklog
             VALUES('hostname', 'ip', 'date')''')
    print(c.lastrowid)
			 
#commit the changes to db			
    conn.commit()
#close the connection
    conn.close()

table_insert("XD","192.168.1.1")

