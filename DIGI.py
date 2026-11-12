# -*- coding: utf-8 -*-


import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Graph Digitizer",
    layout="wide"
)

st.title("Graph Digitizer")

st.write("test")

# Upload a graph image
uploaded_image = st.file_uploader(
    "Upload your graph image",
    type=["png", "jpg", "jpeg", "bmp", "tif", "tiff", "webp"]
)

# Display the uploaded image
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption=uploaded_image.name)
else:
    st.info("Upload an image to get started.")
