import streamlit as st

picture = st.camera_input("Take a picture", on_change=None, args=None, kwargs=True)

if picture:
    st.image(picture)
