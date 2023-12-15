# streamlit run astronomy-image-of-the-day.py
import requests
import streamlit as st

# Prepare API key and API url
api_key = "mTHb8FxSQff65biI2yQ4feDemM8O5x5v8V9es7dQ"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the image title, url and, explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
# The wb indicates that the file is opened for writing in binary mode.
# to read that jpg file you need to use 'rb'
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
