import cv2
import time
from PIL import Image
from model import predict

@st.cache(allow_output_mutation=True)
def get_cap():
    return cv2.VideoCapture(0)

cap = get_cap()

frameST = st.empty()
param=st.sidebar.slider('chose your value')

while True:
    #ret, frame = cap.read()
    _, img = cap.read()
    time.sleep(1)
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    image_loc.image(img)
    # Stop the program if reached end of video
    if not ret:
        print("Done processing !!!")
#         cv.waitKey(3000)
        # Release device
        cap.release()
        break

    frameST.image(frame, channels="BGR")
