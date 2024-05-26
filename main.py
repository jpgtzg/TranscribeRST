# Written by Juan Pablo Gutiérrez

import whisper

model = whisper.load_model('base')

audio = whisper.load_audio('audio.wav')
audio  = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

options = whisper.DecodingOptions(fp16=False)
result = whisper.decode(model, mel, options)

print(result.text)
