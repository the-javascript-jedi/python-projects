import streamlit as st

st.set_page_config(layout="wide")

col1,col2 =st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("the-javascript-jedi")
    content="""
    Hi I am the-javascript-jedi and I am also Batman learning python and docker I am a front end developer wanting to transition to backend
    """
    st.info(content)