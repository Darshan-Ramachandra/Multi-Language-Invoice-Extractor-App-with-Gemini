from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found. Please set GOOGLE_API_KEY in your environment variables.")
else:
    genai.configure(api_key=api_key)

def get_gemini_response(user_input, image, prompt):
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    response = model.generate_content([user_input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

user_input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)


submit = st.button("Tell me about the image")

input_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices &
you will have to answer questions based on the input image
"""

if submit:
    if not uploaded_file:
        st.error("Please upload an image file before submitting.")
    else:
        try:
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(user_input, image_data, input_prompt)
            st.subheader("The Response is")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
