# to run page -- streamlit run main.py
import streamlit as st
import pandas;

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hi, I am the javascript jedi! I am a Python programmer.
    """
    st.info(content)
content2="""Below you can find some of the apps I have built in python, please feel free to contact me"""
st.write(content2)

col3,col4=st.columns(2)
df=pandas.read_csv("data.csv")
with col3:
    # [:10] - last 10
    for index,row in df[:10].iterrows():
        st.header(row["role"])
        st.write(row["first name"])
        st.image("images/"+row["image"])
with col4:
    # df[10:] - first 10
    for index,row in df[10:].iterrows():
        st.header(row["role"])
        st.write(row["last name"])
        st.image("images/"+row["image"])