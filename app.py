import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Step 2
course_images = {
    "Course A": [
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(1).jpg",
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(2).jpg",
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(3).jpg"
    ],
    "Course B": [
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/boring-portfolio/boring+(1).jpg",
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/boring-portfolio/boring+(2).jpg",
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/boring-portfolio/boring+(3).jpg"
    ]
}

# Step 4
def display_images(urls):
    for url in urls:
        response = requests.get(url)
        image_content = response.content
        image = Image.open(BytesIO(image_content))
        st.image(image, caption=url)

# Step 3
selected_course = st.selectbox("Select a course:", list(course_images.keys()))
selected_images = course_images[selected_course]
display_images(selected_images)
