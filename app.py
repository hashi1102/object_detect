import streamlit as st
import cv2
import time
from PIL import Image
from model import predict


st.title("Webカメラでストリーム再生")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("カメラを開けません")

while True:
    ret, frame = cap.read()

    if not ret:
        st.error("フレームを読み込めません")

    # OpenCVのBGR形式からRGB形式に変換
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Streamlitでフレームを表示
    st.image(frame, channels="RGB")

cap.release()
