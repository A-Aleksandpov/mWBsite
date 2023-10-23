import requests
import streamlit as st
from PIL import Image

#doesnt work with currect free website
#wave_img = ImageTk.PhotoImage(Image.open("wave1.png"))

#need photos
st.set_page_config(page_title="Experimental Webpage", page_icon=":tada:", layout="wide")

#head
st.subheader ("Hi, i am Anton Aleksandrov.") #should be img
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

 
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/A.Aleksandpov@yandex.ru" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
