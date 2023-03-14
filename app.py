import torch
import cv2
import numpy as np
import streamlit as st
import time
from PIL import Image


model = torch.hub.load('ultralytics/yolov5', 'yolov5s') 
st.markdown("# Object detection")
with st.spinner():
    img = st.camera_input("Take a picture")


# device = '0'
# with st.spinner():
#     if device.isnumeric():
#         device = int(device)
#     # cap = cv2.VideoCapture(device)

#     image_loc = st.empty()
#     with st.empty():
#         # while cap.isOpened:
#         #     _, img = cap.read()
#         # time.sleep(0.5)
#         img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#         # image_loc.image(img)

#         if img is not None:
#             result = model(img)
#             #result.render()
#             #st.write(result)
#             for result in results[:n_top]:
#                 r = "判定結果 : " + str(round(result[2]*100, 2)) + "%の確率で" + result[0] + "です。"
#                 st.write(f'{r}')


    if img is not None:
        # To read image file buffer as bytes:
        img = Image.open(img)
        result = model(img)
        st.write(result)
        # Check the type of bytes_data:
        # Should output: <class 'bytes'>
