import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

# # This key will serve all examples in this document.
# KEY = "c465067a805d40ffaa0b739cb41d4588"

# # This endpoint will be used in all examples in this quickstart.
# ENDPOINT = "https://west-spike-test.cognitiveservices.azure.com/"

# face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# single_face_image_url = "https://d1qsx5nyffkra9.cloudfront.net/sites/default/files/article-image/eminence-organics-acne-face-mapping.jpg"
# single_image_name = os.path.basename(single_face_image_url)

# detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03')

# print('Detected face ID from', single_image_name, ':')
# for face in detected_faces: print (face.face_id)

# first_image_face_ID = detected_faces[0].face_id

# print(detected_faces.keys)
image = input("enter url: ")

endpointURL = "https://west-spike-test.cognitiveservices.azure.com/face/v1.0/detect?returnFaceAttributes=emotion"
body = {
    "url": image
}

x = requests.post(endpointURL, json = body, headers = {"Ocp-Apim-Subscription-Key": "c465067a805d40ffaa0b739cb41d4588", "Content-Type": "application/json"})

emotions = x.json()[0]['faceAttributes']['emotion']
emotionsDictionary = json.loads(emotions)

print(emotionsDictionary)

# for emotion in sorted(emotions):
#     print(emotion, emotions[emotion])


# print("anger =", emotions['anger'])