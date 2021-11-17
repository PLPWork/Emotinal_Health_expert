from utilss import combine_all
import tensorflow as tf
import streamlit as st
from tensorflow import keras
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config(
     page_title="UTrack",
     layout="wide"
)
st.title("UTrack")

st.subheader('*Analysing Twitter Users on Tweet-to-Tweet basis to track levels of Loneliness, Stress & Anxiety*')

raw_text = st.text_input("Enter the exact twitter handle of the Personality (without @)")
st.text(raw_text)
if raw_text == '':
  st.text('OOPS!!!! Enter userID')
else:
  combine_all(raw_text)

  
