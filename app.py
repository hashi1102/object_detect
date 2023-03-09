import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import time
import av
from PIL import Image
from model import predict

st.title("Camera app")


def callback(frame):
    with st.spinner():
        image_loc = st.empty()
        with st.empty():
#             while cap.isOpened:
#                 _, img = cap.read()
            time.sleep(1)
            img = frame.to_ndarray(format="bgr24")
            img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)


#                 img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#                 image_loc.image(img)

#             if img is not None:

            # # 予測
            results = predict(img)

            # 結果の表示
            n_top = 3  # 確率が高い順に3位まで返す
            for result in results[:n_top]:
                r = "判定結果 : " + str(round(result[2]*100, 2)) + "%の確率で" + result[0] + "です。"
                st.write(f'{r}')
#                 if cv2.waitKey(1) & 0xFF == ord("q"):
#                     break
    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=callback)



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
