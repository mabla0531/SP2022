#!/usr/bin/env python

from time import gmtime, strftime
import simplejson as json
import os
import ACA

#get AWS Client API specs
client = ACA.get_client()

def init_file():
    if (not os.path.isfile('faces.txt')):
        with open('faces.txt', 'w') as init_file:
            init_file.write('Date | Label | Collection | FaceId | ImageId\n')             

def register_profile(image_id, label):
    
    client = get_client()

    init_file()

    with open(image_id, 'rb') as image:
        response = client.index_faces(Image={'Bytes': image.read()}, CollectionId='home', ExternalImageId=label, DetectionAttributes=['ALL'])

        with open('faces.txt', 'a') as file:
            current = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            file.write(('%s | %s | %s | %s | %s\n') % (current, label, 'home', response['FaceRecords'][0]['Face']['FaceId'], response['FaceRecords'][0]['Face']['ImageId']))
