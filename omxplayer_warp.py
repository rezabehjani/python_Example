#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
import time
from PIL import Image 
import os
import pygame

os.system('xset dpms force off')
time.sleep(5)
VIDEO_PATH = Path("2.mp4")

player = OMXPlayer(VIDEO_PATH)
player.can_set_fullscreen()

pos = player.position()
print(pos)
time_end = player.duration()
print(time_end)
time.sleep(time_end)

player.quit()

#os.system('xset dpms force off')

#os.system('xset dpms force off')

time.sleep(5)
VIDEO_PATH = Path("1.mp4")

player = OMXPlayer(VIDEO_PATH)

pos = player.position()
print(pos)
time_end = player.duration()
print(time_end)
time.sleep(150)
player.quit()

os.system('xset dpms force off')



