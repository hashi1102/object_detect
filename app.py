def main():
#     st.markdown("# Image Classification app using Streamlit")
#     st.markdown("model = MobileNetV2")
    device = user_input = st.text_input("input your video/camera device", "0")
    if device.isnumeric():
        device = int(device)
    cap = cv2.VideoCapture(device)
    classifier = Classifier(top_k=5)
    label_names_st = st.empty()
    scores_st = st.empty()
    image_loc = st.empty()

    while cap.isOpened():
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = classifier.predict(frame)
        labels = []
        scores = []
        for (_, label, prob) in result[0]:
            labels.append(f"{label: <16}")
            s = f"{100*prob:.2f}[%]"
            scores.append(f"{s: <16}")
        label_names_st.text(",".join(labels))
        scores_st.text(",".join(scores))
        image_loc.image(frame)
        if cv2.waitKey() & 0xFF == ord("q"):
            break
    cap.release()


if __name__ == "__main__":
    main()
