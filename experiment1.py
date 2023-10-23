import streamlit as st

wave_img = ImageTk.PhotoImage(Image.open("wave1.png"))

#need photos
st.set_page_config(page_title="Experimental Webpage", page_icon=":tada:", layout="wide")

#head
st.subheader ("Hi, i am Anton wave_img")
st.title ("A programmer From Russia")
st.write("I am passionate about finding ways to use Python in Data analytics")
st.write("[Learn More >](https://github.com/A-Aleksandpov)")

