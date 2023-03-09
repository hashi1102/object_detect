import cv2
import time
from PIL import Image
from model import predict

# @st.cache(allow_output_mutation=True)
def get_cap():
    return cv2.VideoCapture(0)

    cap = get_cap()

    image_loc = st.empty()
    with st.empty():
        while cap.isOpened:
            _, img = cap.read()
            time.sleep(1)
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            image_loc.image(img)
        # Stop the program if reached end of video
            if img is not None:

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

if __name__ == "__main__":
    get_cap()
