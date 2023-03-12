import streamlit as st
import cv2 as cv

cap = cv.VideoCapture(-1)

frameST = st.empty()
param=st.sidebar.slider('chose your value')

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
