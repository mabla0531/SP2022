#!/usr/bin/env python

import boto3 as b3
from argparse import ArgumentParser
from time import gmtime, strftime
import numpy as np
from picamera import PiCamera
import cv2
from database_interface import check_attendance
from datetime import datetime

camera = PiCamera()
camera.resolution = (320, 240)

def get_client():
    return b3.client("rekognition", aws_access_key_id="AKIAZ3FOPVTAMAOXUQG5", aws_secret_access_key="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", region_name="us-east-2")

def get_args():
    parser = ArgumentParser(description='Compare an image')
    parser.add_argument('-i', '--image')
    parser.add_argument('-c', '--collection')
    return parser.parse_args()

def check_face(client):
    image = np.empty((240, 320, 3), dtype=np.uint8)
    camera.capture(image, 'rgb')
    success, image = cv2.imencode('.jpg', image)
    image = image.tobytes()

    face_detected = False
    response = client.detect_faces(Image={'Bytes': image})
    if (not response['FaceDetails']):
        face_detected = False
    else:
        face_detected = True

    return face_detected, response

def check_matches(client, collection):
    face_matches = False
    image = np.empty((240, 320, 3), dtype=np.uint8)
    camera.capture(image, 'rgb')
    success, image = cv2.imencode('.jpg', image)
    image = image.tobytes()

    response = client.search_faces_by_image(CollectionId=collection, Image={'Bytes': image}, MaxFaces=1, FaceMatchThreshold=85)
    if (not response['FaceMatches']):
        face_matches = False
    else:
        face_matches = True

    return face_matches, response

def main():
    args = get_args()

    client = get_client()

    print ('[+] Running face checks against image...')
    result, resp = check_face(client)

    if (result):
        print ('[+] Face(s) detected with %r confidence...' % (round(resp['FaceDetails'][0]['Confidence'], 2)))
        print ('[+] Checking for a face match...')
        resu, res = check_matches(client, args.collection)
        currentTime = datetime.now().strftime("%H:%M").split(":")

        if (resu):
            print ('[+] Identity matched [%s] with %r similarity and %r confidence...' % (res['FaceMatches'][0]['Face']['ExternalImageId'], round(res['FaceMatches'][0]['Similarity'], 1), round(res['FaceMatches'][0]['Face']['Confidence'], 2)))
            check_attendance(res['FaceMatches'][0]['Face']['ExternalImageId'], currentTime)
        else:
            print ('[-] No face matches detected...' )

    else :
        print ("[-] No faces detected...")

if __name__ == '__main__':
    main()
