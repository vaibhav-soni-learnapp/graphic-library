import streamlit as st
from PIL import Image
import requests
from io import BytesIO

base_url = "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis"
for i in range(1, 30):
url = base_url + str(i) + ".jpg"
print(url)

# Step 2
course_images = {
    "Course A": [
    print(url)
        

    ],
    "Course B": [
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/boring-portfolio/boring+(1).jpg",
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/boring-portfolio/boring+(2).jpg",
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/boring-portfolio/boring+(3).jpg"
    ],
    "Course C": [
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/cash-flow-statement/cashflow+(1).jpg",
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/cash-flow-statement/cashflow+(2).jpg",
        "https://graphics-library-project.s3.amazonaws.com/graphic+library/cash-flow-statement/cashflow+(3).jpg"
    ]
}

# Step 4
def display_images(urls):
    for url in urls:
        response = requests.get(url)
        image_content = response.content
        image = Image.open(BytesIO(image_content))
        st.image(image, width=500)

# Step 3
selected_course = st.selectbox("Select a course:", list(course_images.keys()))
selected_images = course_images[selected_course]
display_images(selected_images)
