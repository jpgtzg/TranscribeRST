# Written by Juan Pablo Gutiérrez
# 26 05 2024

import whisper
from pydub import AudioSegment

# Loads the model and transcribes the audio file
def get_transcription(audio_file):    
    model = whisper.load_model('base')
    
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

    return text_string

