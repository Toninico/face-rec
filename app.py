import streamlit as st
import cv2
import urllib.request
import numpy as np
import os
import base64

# Title of the web app
st.title("Detect Faces and Download Face Images")

# Create face detection model object
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Upload image function
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image file contents
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.3, minNeighbors=5)

    # Display number of faces detected
    st.write("Number of Faces Detected:", len(faces))

    # Loop through the faces and save each face as a separate image file
    for i, (x, y, w, h) in enumerate(faces):
        # Crop face from the image
        face_crop = image[y:y+h, x:x+w]

        # Encode image in base64 format
        face_bytes = cv2.imencode('.jpg', face_crop)[1].tobytes()
        face_base64 = base64.b64encode(face_bytes).decode()

        # Display face image
        st.image(face_crop, caption="Face {}".format(i), use_column_width=True)

        # Create link to download face image
        href = f'<a download="face_{i}.jpg" href="data:image/jpg;base64,{face_base64}">Download Face {i} Image</a>'
        st.markdown(href, unsafe_allow_html=True)