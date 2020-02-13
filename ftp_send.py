from ftplib import FTP


ftp = FTP('136.243.87.101')
ftp.login('reza', '19972910')
#show list file in ftp
ftp.dir()
#cd to file in ftp
ftp.cwd("/files")
ftp.dir()

fp = open("D:\\music Reza\\video\\Baran - Tazahor [1080].mp4", 'rb')
# upload file

ftp.storbinary("STOR Tazahor.mp4", fp, 1024)
fp.close()
print("ok send")

#file = open('kitten.jpg','rb')
#ftp.storbinary('STOR kitten.jpg', file)
