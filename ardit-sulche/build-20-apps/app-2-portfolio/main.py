import streamlit as st

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
