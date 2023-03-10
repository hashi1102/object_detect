# import streamlit as st
# import cv2
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
import cv2
import time
from PIL import Image
from model import predict



st.markdown("# Camera Application")

device = '0'
with st.spinner():
    if device.isnumeric():
        device = int(device)
    cap = cv2.VideoCapture(device)

    image_loc = st.empty()
    with st.empty():
        while cap.isOpened:
            _, img = cap.read()
            time.sleep(1)
            img = Image.fromarray(img)
            image_loc.image(img)

#             if img is not None:

            # # 予測
            results = predict(img)

            # 結果の表示
            n_top = 3  # 確率が高い順に3位まで返す
            for result in results[:n_top]:
                r = "判定結果 : " + str(round(result[2]*100, 2)) + "%の確率で" + result[0] + "です。"
                st.write(f'{r}')
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
