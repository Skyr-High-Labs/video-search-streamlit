from typing import Sequence
import streamlit as st
from helpers import *

st.title("Video Search Engine")

st.write("As this app is in beta, we are currently only providing search functionality in YouTube videos. Paste the link of the video below, and your search query.")

video_url = st.text_input("YouTube URL", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

search_query = st.text_input("Text input", "shadow on a beach")

# call API
algoHelper = AlgoHelper()
answer = algoHelper(search_query)

# print answer
st.write(f"Expected: hello {search_query}")
st.write(f"Got: {answer}")
if answer == f"hello {search_query}":
    st.success("API works!")
    
else:
    st.warning("API did not work!")


# display algorithm output, e.g. timestamps and screenshots
