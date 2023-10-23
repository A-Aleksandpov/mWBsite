import requests
import streamlit as st
from PIL import Image

wave_img = ImageTk.PhotoImage(Image.open("wave1.png"))

#need photos
st.set_page_config(page_title="Experimental Webpage", page_icon=":tada:", layout="wide")

#head
st.subheader ("Hi, i am Anton wave_img")
st.title ("A programmer From Russia")
st.write("I am passionate about finding ways to use Python in Data analytics")
st.write("[Learn More >](https://github.com/A-Aleksandpov)")

#What i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."
           """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

 
