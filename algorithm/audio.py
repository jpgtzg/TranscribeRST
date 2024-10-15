# Written by Juan Pablo Gutiérrez
# 26 05 2024

import whisper
import os
from pydub import AudioSegment
from openai import OpenAI

import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI"]["OPENAI_API_KEY"])

# Loads the model and transcribes the audio file
def get_transcription(audio_file):    
    model = whisper.load_model('turbo')
    
    # Convert the audio file to a format that Whisper can process
    audio = AudioSegment.from_file(audio_file, format='mp3')
    audio.export('temp.mp3', format='mp3')

    # Load the audio file for Whisper
    audio_data = whisper.load_audio('temp.mp3')

    options = {
        "language": "en",
        "task": "translate" 
    }

    result = whisper.transcribe(model, audio_data, **options, fp16=False)

    text_value = result.get('text', '')

    text_string = str(text_value)

    os.remove('temp.mp3')

    return text_string


def get_openai_transcription(audio_file):
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print(transcription.text)
    return transcription.text
