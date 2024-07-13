
import streamlit as st
import google.generativeai as genai
import PIL.Image
import os
import pyttsx3

# Set API key
genai.configure(api_key="AIzaSyD2BOlrc0AdS4RxN_JDhZtn5YK-XizmAAI")

# Initialize text-to-speech engine
tts = pyttsx3.init()

# Create Streamlit app
st.title("NOVA Text and Image Analyzer")

# Get user input
text = st.text_input("Enter the prompt:")

# Ask user if they want to hear the text spoken
speak = st.selectbox("Do you want to hear the text spoken?", ("Yes", "No"))

# Upload image
uploaded_img = st.file_uploader("Upload an image", type=["jpg", "png"])

# Display uploaded image
if uploaded_img:
    img = PIL.Image.open(uploaded_img)
    st.image(img, caption="Uploaded Image")

# Generate text using Gemini model
if st.button("Generate Text"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(text)
    generated_text = response.text
    st.write(generated_text)
    if speak == "Yes":
        tts.say("The generated text is: " + generated_text)
        tts.runAndWait()

# Generate text using Gemini model for image analysis
if st.button("Analyze Image"):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(["What is in this photo?", img])
    st.write(response.text)