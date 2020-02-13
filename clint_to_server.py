import os
import ftplib
import socket
from tqdm import tqdm
import time
global ftp

def FTP_GLOB_transfer(URL, UserName, Password, File_name):

    ftp = ftplib.FTP(URL, UserName, Password)   # connect to host, default port
    print (URL, UserName, Password)
    ftp.cwd("/files")
    ftp.dir()
    FileName = File_name
    filesize = os.path.getsize(File_name)
    print("file size = :", filesize)
    TheFile = open(File_name, 'rb')
    with tqdm(unit = 'blocks', unit_scale = True, leave = False, miniters = 1, desc = 'Uploading...... ', total = filesize) as tqdm_instance:
        ftp.storbinary('STOR ' + FileName, TheFile, 2048, callback = lambda sent: tqdm_instance.update(len(sent)))
    TheFile.close()
    ftp.quit()
    print("All File send")



def send_socket(host, port, masage):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(masage.encode('utf-8'))
        s.close()



def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False


ID_Device = input("Enter ID Devise (EX: 1001) :")
file_name = input("Enter name file : (EX: test.mp4) ")

#Mon Feb 15 09:34:03 2016
Time_Update = input("Enter Time Update Device (EX: 24:34) ")


if (isTimeFormat(Time_Update) == True):
    time_play = input("Enter time for play movies (EX: 09:34): ")
    if (isTimeFormat(time_play) == True):

        massage_send = '>>,' + ID_Device + ',' + file_name + ',' + time_play + ',' + Time_Update
        print(massage_send)
        send_socket('136.243.87.101', 2020, massage_send)
        FTP_GLOB_transfer('136.243.87.101', 'reza', '19972910', file_name)


    else:
        print(time_play, "Time is not Exept ", "(EX: 24:34)")

else:
    print(Time_Update, "Time Update is not Exept ", "(EX: 24:34)")


