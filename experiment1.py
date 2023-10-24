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

#who am i
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who am i")
        st.write("##")
        st.write(
            """
            
            - I realized that I want to become a Python programmer.
            - I am interested in all possible areas where this language can be applied, in particular, data science and machine learning. I am open to learning new technologies.
            - Touching and participating in the development of large and interesting projects is what really got me interested in programming. I am focused on solving problems and implementing quality and beautiful code using modern design standards.
            - Soft skills: multitasking, teamwork, time management.
            - My main focus is Python; SQL; Django; Pytorch; Pyspark; MLflow; Golang, Matplotlib, Numpy, Scipy, Streamlit, Random, Tkinter, PyQt5, math, pandas, sklearn, seaborn.
           """
        )

#other info
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My pet project and other skills")
        st.write("##")
        st.write(
            """
            
            * Program to collect data from website using bs4, numpy, space, trafilatura, to csv file requests.
            * Program to analyze excel file using numpy, pandas, seaborn, sklearn, xgboost.
            * Program to transfer file to google cloud. Using pydrive, google-cloud-storage, pandas modules.
            * Personal website.
            * Browser using PyQt5 module.
            * Notepad using tkinter module.
            * Rock, scissors, paper game with the help of tkinter, random modules.
            * Engineering calculator using tkinter, pygame, speechrecognition modules. Responds to voice commands.
            * Tetris with pygame, math, random, pathlib, sys.
            * Chat via socket module.
            * 3D snake with ursina and random modules.
            * Gaming machine with the help of random module.

                    Skills and abilities:
            * Project management: Github.
            * Work with large volumes of information.
            * Data analysis.
            Text editors and integrated development environment: Microsoft Word, MS Visual Studio Code, docker, MS Office.

           """
        )

 



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
            - are working with Excel and found themselves thinking - "there has to be a better way.
           """
        )

# just for myself <textarea name="message" placeholder="Your message here" required></textarea>
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/a.aleksandpov@yandex.ru" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <input type="message" name="message" placeholder="Your message here" required>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QN3G7DEJLL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-QN3G7DEJLL');
</script>
