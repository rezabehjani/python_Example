#https://realpython.com/python-speech-recognition/
import speech_recognition as sr


#https://pythonbasics.org/convert-mp3-to-wav/
#apt-get install ffmpeg
from os import path
from pydub import AudioSegment


from threading import Thread as th

# files
src = "AUDIO_FILE.mp3"
dst = "test.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

sound2 = AudioSegment.from_file("aa.mp4", "mp4")
sound2.export(dst, format="wav")


r = sr.Recognizer()


def t1():
    cou = 1
    while True:
        cou += 1

        with sr.AudioFile('test.wav') as source:
            audio2 = r.record(source)
        print(r.recognize_google(audio2, language='fa'))
        print(cou)


t = th(target=t1)
t.start()

t2 = th(target=t1)
t2.start()

t3 = th(target=t1)
t3.start()
