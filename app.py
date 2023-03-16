import streamlit as st
import requests
from io import StringIO
import os
import numpy as np
import pandas as pd
from PIL import Image
import datetime

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(page_icon=":eye:", page_title = "AI iEye", layout="wide")

#Remove the Menu Button and Streamlit Icon
hide_default_format = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_default_format, unsafe_allow_html=True)

prediction = None
response = None

def call_api():
    url = 'https://odr-jzvmjlq27a-ew.a.run.app/predict'
    file = {'file': uploaded_file}
    response = requests.post(url, files=file)
    prediction = response.json()
    st.text("Eye-Eye Captain!")
    st.markdown("<br>",unsafe_allow_html=True)
    st.write("""### Patient's Results:""")
    st.markdown("<br>",unsafe_allow_html=True)
    if prediction['cataract'] >= 50 or prediction['glaucoma'] >= 50 or prediction['myopia'] >= 50:
        st.write('''##### :warning: **We recommend a more detailed examination!**''')
    else:
        st.write('''##### :thumbsup: **Looking healthy!**''')
    st.markdown("<br>",unsafe_allow_html=True)

    if prediction['cataract'] >= 50:
        st.write(f'''
        * Probablity of having **cataract**: :red[{prediction['cataract']}%]''')
    else:
        st.write(f'''
        * Probablity of having **cataract**: :green[{prediction['cataract']}%]''')
    st.markdown("<br>",unsafe_allow_html=True)

    if prediction['glaucoma'] >= 50:
        st.write(f'''
        * Probablity of having **glaucoma**: :red[{prediction['glaucoma']}%]''')
    else:
        st.write(f'''
        * Probablity of having **glaucoma**: :green[{prediction['glaucoma']}%]''')
    st.markdown("<br>",unsafe_allow_html=True)

    if prediction['myopia'] >= 50:
        st.write(f'''
        * Probablity of having **myopia**: :red[{prediction['myopia']}%]''')
    else:
        st.write(f'''
        * Probablity of having **myopia**: :green[{prediction['myopia']}%]''')
    st.markdown("<br>",unsafe_allow_html=True)


#Defining columns
c_left, c_right = st.columns(2, gap="large")

with c_left:
    st.title("Ocular Disease Recognition")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Upload an eye fundus image!")
    st.write("Deep Learning model for image recognition\ntrained to predict the probability of having:\n\n- cataract\n- glaucoma\n- myopia")
    st.text("(Powered by VGG19)")

    #Uploading an image
    uploaded_file = st.file_uploader("***Upload Image:***", type=["jpg", "jpeg", "png"])
    st.markdown("<br>",unsafe_allow_html=True)


    if uploaded_file is not None:
        image_file = uploaded_file
        img = Image.open(image_file)
        st.image(uploaded_file, width=50)
        report = st.empty()
        if st.button("Make Prediction" + " " + ":game_die:"):
            call_api()

    st.markdown("<br><br><br><br><br>",unsafe_allow_html=True)
    logo_img = Image.open("logo.png")
    st.image(logo_img, width=200, channels='RGB',output_format=' ')
    st.write("""**Authors**: João Pimenta, João Santos, Maureen Dupret, Sara Vaz""")
    st.write("""*Data Science Batch #1157 Lisbon, 2023*""")


with c_right:
    st.write('')
    st.write('')
    page_img = Image.open("image.png")
    st.image(page_img, width=450, channels='RGB',output_format='auto')
    st.markdown("<br><br><br>",unsafe_allow_html=True)

    m = st.markdown("""
        <style>
        div.stButton > button:first-child {
        background-color: rgb(238, 159, 24);
        color: white;
        height: 3em;
        width: 15em;
        }</style>""", unsafe_allow_html=True)
