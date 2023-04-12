import streamlit as st
from Functional import GetResult

def set_page() : return st.set_page_config(page_title="DL", layout="wide")

def get_data() : return GetResult().get_result()

def user_interface():
    set_page()
    st.title("독산 서선생의 서시.....")
    "https://cc5547-project-glamping-dl-projectmain-3qqcfu.streamlit.app/"
    st.dataframe(get_data())