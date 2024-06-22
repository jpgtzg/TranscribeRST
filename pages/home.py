# Written by Juan Pablo Gutiérrez
# 20 06 2024

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from algorithm import audio, code_converter

def __init__ ():
    st.set_page_config(page_title="AI Docs", page_icon="🧠")
    pass

st.title("AI Docs")

st.write("""Welcome to AI Docs! 
         This is a platform where you can upload lecture or meeting recordings to get 
         documentation code in *.rst* fie format for you Sphinx projects, enhancing the 
         overall documentation-making process and achieving a more efficient workflow.""")

st.write ("To get started, upload an audio file in *.mp3* format and click the 'Transcribe' button.")

uploaded_file = st.file_uploader("Choose a file", type=['mp3'])
transcribe_button = st.button("Transcribe")

if uploaded_file and transcribe_button: 
    st.write("Transcribing..")
    
    transcription = audio.get_transcription(uploaded_file)
    code = code_converter.get_code(transcription)
    
    st.write("Transcription:")
    st.write(transcription)
    
    st.write("Code:")
    st.write(code)
    
    
st.write("Credits: Juan Pablo Gutiérrez, 2024")