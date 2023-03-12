import streamlit as st

picture = st.camera_input("Take a picture", disabled=True)

if picture:
    st.image(picture)
