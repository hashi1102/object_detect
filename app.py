import streamlit as st
import cv2 as cv
from PIL import Image

cap = cv.VideoCapture(0)

frameST = st.empty()

with st.spinner():
    while True: 
        ret, frame = cap.read()
        # Stop the program if reached end of video
        if not ret:
            print("Done processing !!!")
            #cv.waitKey(3000)
            # Release device
            cap.release()
            break

        frameST.image(frame, channels="BGR")
