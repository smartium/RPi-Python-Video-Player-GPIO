import RPi.GPIO as GPIO
import time
import os
import sys
from subprocess import Popen

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

movie = ("/home/pi/Desktop/Video/video.mp4")
image = ("/home/pi/Desktop/Imagem/wallpaper.png")
playing = True

Popen(['ffplay', '-loop', '0', '-loglevel', 'quiet', movie])

while True:
    input_state = GPIO.input(23)
    if input_state == False:
      if playing:
        playing = False
        os.system('killall ffplay')
        os.system('tput reset')
        Popen(['ffplay', '-loop', '0', '-loglevel', 'quiet', image])
      else:
        playing = True
        os.system('killall ffplay')
        os.system('tput reset')
        Popen(['ffplay', '-loop', '0', '-loglevel', 'quiet', movie])
      time.sleep(2)