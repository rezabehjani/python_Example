import ftplib

def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
    except:
        print("Error")


ftp = ftplib.FTP("136.243.87.101")
ftp.login("reza", "19972910")
ftp.cwd('/files')  # change directory to /pub/
ftp.dir()
getFile(ftp, 'test.txt')
ftp.quit()