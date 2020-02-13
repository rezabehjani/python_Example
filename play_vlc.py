import vlc 
import time
import sqlite3


while (True):
    #print (time.asctime( time.localtime(time.time()) ))
    #conn = sqlite3.connect('list_play.db')
    #print ("Opened database successfully")
    #cursor = conn.execute("SELECT time from time_play where id==1")
    #tim = time.asctime(time.localtime(time.time()) )
    if (1 == 1):

        instance = vlc.Instance()



        #Create a MediaPlayer with the default instance
        player = instance.media_player_new()

        #Load the media file
        media = instance.media_new('/home/reza/ftp/files/Gaston.Lagaffe.2018.mkv')

        #Add the media to the player
        player.set_media(media)

        #Play for 10 seconds then exit
        player.play()
        break

