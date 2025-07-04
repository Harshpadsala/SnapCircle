import cv2
import os
import face_recognition
import pickle
import numpy as np

print("Loading Encode File ...")
with open('EncodeFile.p', 'rb') as file:
    existing_list = pickle.load(file)

given_id="lakkad"

existing_encoding, existing_id = existing_list
print("Encode File Loaded")

# print(existing_encoding)

if given_id in existing_id:
    index=existing_id.index(given_id)
    encoding=[existing_encoding[index]]

path_to_images = "/Users/harshpadsala/SnapCircle/testing_photo" # Path to the folder where images are stored.
myList = os.listdir(path_to_images) # Retrieves the list of all image filenames in that folder.
images=[] # Initializes an empty list to store the names of recognized images.

for img_name in myList:
    img = cv2.imread(f'{path_to_images}/{img_name}')
    imgS = cv2.resize(img, (0, 0), None, 0.5, 0.5) # Resizes the image to half its original size
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB) # Converts the image from BGR to RGB

    faceLoc = face_recognition.face_locations(imgS) # Detects faces in the resized image and returns their coordinates.
    encodeCurFrame = face_recognition.face_encodings(imgS, faceLoc) # Generates face encodings for detected faces.

    # Sets a threshold for face recognition similarity.
    # A lower value means stricter matching (less chance of false positives).
    # A higher value means looser matching (higher chance of incorrect matches).
    RECOGNITION_THRESHOLD = 0.50  # Adjust this value as needed

    # Check if any face is detected
    if faceLoc:
        for encodeFace, facePosition in zip(encodeCurFrame, faceLoc):
            # Compare the detected face with known faces
            matches = face_recognition.compare_faces(encoding, encodeFace)
            faceDis = face_recognition.face_distance(encoding, encodeFace)
            
            # Find the best match
            matchIndex = np.argmin(faceDis)
            # print(faceDis[matchIndex])
            
            if matches[matchIndex] and faceDis[matchIndex] < RECOGNITION_THRESHOLD:
                # If a match is found and below the threshold, retrieve the ID and display
                matchedId = given_id
                images.append(img_name)
                print(f"Face recognized: {matchedId}")
                
            else:
                continue
    else:
        continue

print(images)

    