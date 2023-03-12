import streamlit as st

picture = st.camera_input("Take a picture", help="aaa")

if picture:
    st.image(picture)
