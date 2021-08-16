from typing import Sequence
import time
import streamlit as st
from helpers import *

st.title("Video Search Engine")

st.write("As this app is in beta, we are currently only providing search functionality in YouTube videos. Paste the link of the video below, and your search query.")


algoHelper = AlgoHelper()

#@st.cache
def callAlgo(url, query):
    return algoHelper({"url":url,
                            "query":query})

def displayResults(url, timestamps):
    st.write(timestamps)
    for timestamp in timestamps:
        st.write(addTimestampToYoutubeURL(url, timestamp))
                            

def timeExecution(start=True):
    key = 'time'
    if start:
        st.session_state.time = time.perf_counter()
        return
    else:
        assert(key in st.session_state)
        perf = time.perf_counter() - st.session_state.time
        del st.session_state[key]
        return perf
        

with st.form(key='main_form'):
    video_url = st.text_input("YouTube URL", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    search_query = st.text_input("Text input", "shadow on a beach")
    submit= st.form_submit_button(label='Submit')


if submit:
    with st.spinner("Submitted your request, wait a few minutes!"):
        timeExecution()
        timestamps = callAlgo(video_url, search_query)
        perf = timeExecution(False)
        st.write(f"This took {perf:0.4f} seconds")
        displayResults(video_url, timestamps)
        
    

# print answer


# display algorithm output, e.g. timestamps and screenshots
