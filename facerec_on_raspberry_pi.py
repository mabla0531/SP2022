# This is a demo of running face recognition on a Raspberry Pi.
# This program will print out the names of anyone it recognizes to the console.

# To run this, you need a Raspberry Pi 2 (or greater) with face_recognition and
# the picamera[array] module installed.
# You can follow this installation instructions to get your RPi set up:
# https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65

import face_recognition
import picamera
import numpy as np
from os import listdir

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
RESX = 1280
RESY = 720
camera.resolution = (RESX, RESY)
output = np.empty((RESX, RESY, 3), dtype=np.uint8)

faces = []

#--------------------------------------------------------------------------------------------
#
# TODO have an index file and parse for file names / profile names, associate with dictionary
#
#--------------------------------------------------------------------------------------------

for filename in listdir():
    faces.append(face_recognition.load_image_file(filename))

# Variables for face recognition
face_locations = []
face_encodings = []

def process_faces():
    for current_face in faces:
        current_face_encoding = face_recognition.face_encodings(current_face)[0]

        face_encodings = face_recognition.face_encodings(output, face_locations)

        # See if the face is a match for the known face(s)
        
        for fe in face_encodings:
            match = face_recognition.compare_faces([current_face_encoding], fe)
            name = "<Unknown Person>"

            if match[0]:
                name = "Barack Obama"

        print("{}'s face recognized.".format(name))


while True:
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    
    if (len(face_locations) > 0)
        process_faces()
