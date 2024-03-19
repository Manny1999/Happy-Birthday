from pathlib import Path

import json

import streamlit as st

from streamlit_lottie import st_lottie

from streamlit_extras.let_it_rain import rain



# Directories and file locations

THIS_DIR = Path(__file__).parent

CSS_FILE = THIS_DIR / "style" / "style.css"

ASSETS = THIS_DIR / "assets"

LOTTIE_ANIMATION = ASSETS / "Birthday.json"



# Functions to help load and display the animation

def load_lottie_animation(file_path):

    with open(file_path, "r") as f:

         return json.load(f)

         

# Functions for fireworks effect



def run_snow_animation():
    rain(emoji="🥳", font_size=20, falling_speed=5, animation_length="infinite")

    

# Function to get name

def get_person_name():

    query_params = st.query_params

    return query_params.get("name", "Abuela")

    

# Page Configuration

st.set_page_config(page_title="Happy Birthday", page_icon="🎉")



# Run birthday animation

run_snow_animation()



#Apply the CSS

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# Display header with name

PERSON_NAME = get_person_name()

st.header(f"Happy Birthday, {PERSON_NAME}! 🎉", anchor=False)



# Dislpay the lottie animation  

lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)

st_lottie(lottie_animation, key="lottie-holiday", height=300)



# Birthday messaged

st.markdown(

    f"Dear {PERSON_NAME}, wishing you a wonderfull birthday filled with joy anf happyness. 🎂"

)
