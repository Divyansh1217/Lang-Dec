from langdetect import detect
import streamlit as st
st.write("Enter any text in any language: ")

st.text(detect(text))
