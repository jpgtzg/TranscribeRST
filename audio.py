# Written by Juan Pablo Gutiérrez
# 26 05 2024

import whisper
from flask import Flask, request
from pydub import AudioSegment
import analysis

app = Flask(__name__)


# Loads the model and transcribes the audio file
@app.route('/get-transcription', methods=['POST'])
def get_transcription():
    audio_file = request.files['audio']
    
    model = whisper.load_model('base')
    
    # Convert the audio file to a format that Whisper can process
    audio = AudioSegment.from_file(audio_file, format='mp3')
    audio.export('temp.mp3', format='mp3')  # Export as WAV file

    # Load the audio file for Whisper
    audio_data = whisper.load_audio('temp.mp3')

    options = {
        "language": "en",
        "task": "translate" 
    }

    result = whisper.transcribe(model, audio_data, **options, fp16=False)

    text_value = result.get('text', '')

    text_string = str(text_value)

    with open('result.txt', 'w') as file:
        file.write(text_string)

    print(text_string)

    analysis.get_topics(text_string)

    return text_string

if __name__ == '__main__':
    app.run(port=5000, debug=True)
