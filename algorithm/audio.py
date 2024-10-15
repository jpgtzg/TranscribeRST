# Written by Juan Pablo Gutiérrez
# 26 05 2024

from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI"]["OPENAI_API_KEY"])

def get_openai_transcription(audio_file):
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )

    return transcription.text
