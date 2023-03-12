import streamlit as st
from threading import Thread
import cv2
import time

cap = cv2.VideoCapture(0)
frameST = st.empty()
param = st.sidebar.slider('choose your value')

stopper_started = False
while True:
    success, frame = cap.read()
    if not success: break

    frameST.image(frame, channels="BGR")
    updated_time = time.time()

    if not stopper_started:
        #this block executes for once with every
        #streamlit re-run command
        def stopper(self):
            while True:
                try:
                    #if time difference increases this thread will be terminated
                    time_diff = round(time.time() - updated_time)
                    if time_diff >1: #1 second
                        print("Done processing !!!")
                        print("Releasing VideoCapture")
                        #if streamlit ui is stopped
                        #time gap will increase
                        #hence releasing camera resource
                        cap.release()
                        break
                except: pass
        th = Thread(target=stopper, args=(0,))
        th.daemon = True
        th.start()
        stopper_started = True
