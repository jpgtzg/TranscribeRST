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

st.markdown("# Transcribe:blue[RTS]") 

def home(): 
    st.markdown("### Welcome to Transcribe:blue[RTS]!")
    st.write(""" 
             This is a platform where you can upload lecture or meeting recordings 
             to get documentation code in *.rst* fie format for you Sphinx projects, enhancing the overall 
             documentation-making process and achieving a more efficient workflow.""")

def upload() : 
    st.markdown("### Upload an audio file")
    st.write ("""Getting started is easy! Simply upload your audio file in .mp3 format,
            and click the 'Transcribe' button. Our advanced transcription service will convert your audio 
            into documentation code, allowing you to focus on what matters most—creating great content""")

    uploaded_file = st.file_uploader("Choose a file", type=['mp3'])

    with st.container(border=True): 
        st.text_input("Enter some context about the audio file", key="context")
        
        transcribe_button = st.button("Transcribe")
        if uploaded_file and transcribe_button: 
            code = ""

            with st.spinner('Transcribing...'):                    
                code = code_converter.get_code(audio.get_openai_transcription(uploaded_file), st.session_state.context)

            st.divider()
            with st.container(border=True): 
            
                st.write("Code: ")
            
                st.code(code)
                
                st.success("Audio file transcribed to RTS succesfully!")
                
home()
upload() 

st.divider()
        
st.write("Credits: Juan Pablo Gutiérrez, 2024")
