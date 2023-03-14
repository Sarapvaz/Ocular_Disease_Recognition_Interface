import streamlit as st
import requests
from io import StringIO
import os
import numpy as np
import pandas as pd
from PIL import Image
import datetime

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(page_icon=":eye:", page_title = "Ocular Disease Recognition", layout="wide")

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

#Defining columns
c_left, c_right = st.columns(2, gap="medium")

with c_left:
    st.title("Ocular Disease Recognition")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Upload an eye fundus!")
    st.text("Deep Learning model trained with over 100.000 parameteres \nto **detect eye diseases**.")
    st.markdown("<br><br><br><br><br>",unsafe_allow_html=True)
    #Uploading an image
    uploaded_file = st.file_uploader("***Upload Image:***", type=["jpg", "jpeg", "png"]) #U+1F447)
    st.markdown("<br>",unsafe_allow_html=True)

    if uploaded_file is not None:
        image_file = uploaded_file
        img = Image.open(image_file)
        st.image(uploaded_file, width=50)
        st.write("#### EYE EYE Captain!")
        b = c_right.button("Make Prediction" + " " + ":game_die:")

with c_right:
    st.write('')
    st.write('')
    img = Image.open("image.jpg")
    st.image(img, width=450, channels='RGB',output_format='auto')
    st.markdown("<br><br><br>",unsafe_allow_html=True)

    m = st.markdown("""
        <style>
        div.stButton > button:first-child {
        background-color: rgb(238, 159, 24);
        color: white;
        height: 3em;
        width: 15em;
        }</style>""", unsafe_allow_html=True)

    if st.button is not None:
        url = 'http://127.0.0.1:8000'
        current_time = datetime.datetime.now()
        temp_image = str(current_time) + "_" + 'img.jpg'
        img.save(temp_image)

        multipart_form_data = {
            "inputImage" : (open(temp_image, "rb"))
        }
        response = requests.post(url, files=multipart_form_data)
        prediction = response.json()

        if os.path.exists(temp_image):
            os.remove(temp_image)

        print(f"{prediction}")


# if prediction:
#         if prediction == 'Normal':
#             st.markdown("""
#                 ### Result:
#                 #####
#                 """)
#             st.write(f'''
#                 Disease: **Normal**
#                 ''')
#             st.write('''
#                 We detect nothing about your eye ! <br>
#                 It looks like **normal** !
#                 ''', unsafe_allow_html=True)
#             st.markdown('''
#                 ##
#                 #####
#                 ''')
#         if "target" in prediction:
#             st.markdown("""
#                 ### Result:
#                 #####
#                 """)

#             df = pd.DataFrame(prediction['target'], index=['G', 'C', 'A', 'H', 'M', 'O' ]).T

#             names = df.columns
#             dict_names = {
#                 'G' : 'Glaucoma',
#                 'C' : 'Cataract',
#                 'H' : 'Hypertension',
#                 'A' : 'Age related Macular Degeneration (A)',
#                 'M' : 'Pathological Myopia',



#Converting clasisfication report to .jpg format
# im2 = Image.open("classification_report")
# rgb_im = im2.convert("RGB")

# #Download the classification report directly from app
# st.download_button(label="Download data as jpg",data=rgb_im,file_name='Classification_Report.jpg')
