# Written by Juan Pablo Gutiérrez
# 26 05 2024

import whisper
import analysis

model = whisper.load_model('base')

audio = whisper.load_audio('audio.wav')
audio  = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

options = whisper.DecodingOptions(fp16=False)
result = whisper.decode(model, mel, options)

with open('result.txt', 'w') as file:
    file.write(result.text)

print(result.text)

#analysis.get_topics(result.text)

