import streamlit as st
import streamlit.components.v1 as components
import base64


# Function to read an image file and convert it to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Get base64 encoded images
background_image = get_base64_image("img/tg_image_1984667092.png")
overlay_image = get_base64_image("img/LOGO2.png")

# HTML content with embedded base64 images
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .image-container {{
            position: relative;
            display: inline-block;
        }}
        .image-container img {{
            display: block;
        }}
        .overlay {{
            position: absolute;
            top: 0;
            left: 0;
            max-width: 462px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="image-container">
        <img src="data:image/png;base64,{background_image}" alt="Background Image">
        <img src="data:image/png;base64,{overlay_image}" class="overlay" alt="Overlay Image">
    </div>
</body>
</html>
"""

# Embed the HTML content in the Streamlit app
components.html(html_content, height=600)
