# import streamlit as st
# import cv2
# import time
# from PIL import Image
# from model import predict
# import numpy as np


# img_file_buffer = st.camera_input("Take a picture")


# if img_file_buffer is not None:
#     # To read image file buffer with OpenCV:
#     bytes_data = img_file_buffer.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

#     # Check the type of cv2_img:
#     # Should output: <class 'numpy.ndarray'>
#     st.write(type(cv2_img))

#     # Check the shape of cv2_img:
#     # Should output shape: (height, width, channels)
#     st.write(cv2_img.shape)

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
