import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import av #strealing video library

st.title('Streamlit App Test')
st.write('Gray Scale')

#Class
class VideoProcessor:
    def recv(self,frame):

        img = frame.to_ndarray(format = 'bgr24')
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = av.VideoFrame.from_ndarray(img, format='gray')

        return img

webrtc_streamer(key='example', video_processor_factory=VideoProcessor)
