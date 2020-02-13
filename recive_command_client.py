# Echo server program
import socket
import sqlite3
import os.path
from os import path

def init_sql():
    conn = sqlite3.connect('sql_socket.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE socket
                 (ID text, File text, Time_Play text, Time_Update text)''')
    # Save (commit) the changes
    conn.commit()
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def update_sql(ID, File, Time_Play, Time_Update):
    conn = sqlite3.connect('sql_socket.db')
    c = conn.cursor()
    c.execute("SELECT * FROM socket WHERE ID = ?", (ID,))
    data = c.fetchone()

    if (data is None):
        c.execute("INSERT INTO socket VALUES (?, ?, ?, ?)", (ID, File, Time_Play, Time_Update))
        # Save (commit) the changes
        conn.commit()
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    else:
        c.execute("UPDATE socket SET ID = ? ,File = ?,Time_play = ?,Time_Update = ? WHERE ID= ? ",
                  (ID, File, Time_Play, Time_Update, ID))
        # Save (commit) the changes
        conn.commit()
        # Just be sure any changes have been committed or they will be lost.
        conn.close()










HOST = ''             # Symbolic name meaning all available interfaces
PORT = 2020           # Arbitrary non-privileged port

if (path.exists('sql_socket.db') == True):
    print("database Exist ")

else:
    init_sql()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('Lisining to : ', socket.gethostname())
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            # byte to str
            data_to_str = data.decode('ASCII')
            print("Recive data = ", data_to_str)
            sql_data = data_to_str.split(',')
            update_sql(sql_data[1], sql_data[2], sql_data[3], sql_data[4])
            if not data: break


