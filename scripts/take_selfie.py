#!/usr/bin/env python

from picamera import PiCamera
import time
import os

count = 5
camera = PiCamera()
camera.vflip = True
camera.hflip = True
directory = '/home/pi/Desktop/SP2022/faces'

if not os.path.exists(directory):
    os.makedirs(directory)

student_id = input("Enter your student id: ")

print ('[+] A photo will be taken in 5 seconds...')

for i in range(count):
    print (count - i)
    time.sleep(1)

milli = int(round(time.time() * 1000))
image = '{0}/{1}.jpg'.format(directory, student_id)
camera.capture(image)
print ('Your image was saved to %s' % image)
