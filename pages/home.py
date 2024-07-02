# Written by Juan Pablo Gutiérrez
# 20 06 2024

import streamlit as st
import sys
from pathlib import Path
import time as t

sys.path.append(str(Path(__file__).resolve().parent.parent))

from algorithm import audio, code_converter

def __init__ ():
    st.set_page_config(page_title="AI Docs", page_icon="🧠")
    pass

st.title("AI Docs")

def home(): 
    st.write("""Welcome to AI Docs! 
            This is a platform where you can upload lecture or meeting recordings to get 
            documentation code in *.rst* fie format for you Sphinx projects, enhancing the 
            overall documentation-making process and achieving a more efficient workflow.""")

def upload() : 
    st.write ("To get started, upload an audio file in *.mp3* format and click the 'Transcribe' button.")

    uploaded_file = st.file_uploader("Choose a file", type=['mp3'])
    transcribe_button = st.button("Transcribe")

    if uploaded_file and transcribe_button: 
        st.write("Transcribing..")
        
        t.sleep(3)
        
        code = code_converter.get_code(audio.get_transcription(uploaded_file))
        with st.container(border=True): 
        
            st.write("Code: ")
        
            st.code(code)

home()
upload() 
        
st.write("Credits: Juan Pablo Gutiérrez, 2024")
