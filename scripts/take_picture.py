#!/usr/bin/env python

from picamera import PiCamera
import time
from tkinter import *
from tkinter import ttk
import os
import register

camera = PiCamera()
camera.vflip = True
camera.hflip = True
directory = '/home/pi/SP2022/faces'

def picture(name):
    if not os.path.exists(directory):
        os.makedirs(directory)

    image = '{0}/{1}.jpg'.format(directory, name)
    camera.capture(image)
    print ('Your image was saved to %s' % image)
