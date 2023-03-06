import streamlit as st
from PIL import Image
import requests
from io import BytesIO


# Step 2
course_images = {
    "Course A": [
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(1).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(2).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(3).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(4).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(5).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(6).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(7).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(8).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(9).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(10).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(11).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(12).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(13).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(14).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(15).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(16).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(17).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(18).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(19).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(20).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(21).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(22).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(23).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(24).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(25).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(26).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(27).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(28).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(29).jpg",
      "https://graphics-library-project.s3.amazonaws.com/graphic+library/technical-analysis/technicalanalysis+(30).jpg"
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
