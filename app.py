import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Step 2
image_urls = [
    "https://graphics-library-project.s3.amazonaws.com/graphic+library/cash-flow-statement/cashflow+(1).jpg",
    "https://graphics-library-project.s3.amazonaws.com/graphic+library/cash-flow-statement/cashflow+(2).jpg",
    "https://graphics-library-project.s3.amazonaws.com/graphic+library/cash-flow-statement/cashflow+(3).jpg"
]

# Step 4
def display_image(url):
    response = requests.get(url)
    image_content = response.content
    image = Image.open(BytesIO(image_content))
    st.image(image, caption=url)

# Step 3
selected_url = st.selectbox("Select an image URL:", image_urls)
display_image(selected_url)
