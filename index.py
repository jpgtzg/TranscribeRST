import os
from pydub import AudioSegment
import whisper
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

model = whisper.load_model('base')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/split-audio', methods=['POST'])
def split_audio():
    try:
        audio_file = request.files['audio']

        # Force file format to .mp3
        audio = AudioSegment.from_file(audio_file, format='mp3')
        
        logging.info(f'Audio file: {audio_file.filename}')

        segment_length = 10 * 60  # Start with 10 minutes
        max_segment_size = 24 * 1024 * 1024  # 24MB in bytes
        prompt = ""
        full_text = ""

        segment_filename = os.path.splitext(audio_file.filename)[0]
        duration = audio.duration_seconds
        number_of_segments = int(duration / segment_length)
        
        logging.info(f'Audio duration: {duration} seconds')

        if number_of_segments == 0:
            number_of_segments = 1

        i = 0
        segment_start = 0
        segment_end = segment_length * 1000

        while segment_start < duration * 1000:
            sound_export = audio[segment_start:segment_end]
            export_format = 'mp3'
            exported_file = f'/tmp/{segment_filename}-{i+1}.{export_format}'
            sound_export.export(exported_file, format=export_format)

            while os.path.getsize(exported_file) > max_segment_size:
                segment_length /= 2  # Halve the segment length
                segment_end = segment_start + segment_length * 1000
                sound_export = audio[segment_start:segment_end]
                sound_export.export(exported_file, format=export_format)

            logging.info(f'Processing segment {i+1}, file: {exported_file}')
            
            # Load audio with Whisper utility
            audio_segment = whisper.load_audio(exported_file)
            logging.debug(f'Audio segment shape: {audio_segment.shape}')
            
            mel = whisper.log_mel_spectrogram(audio_segment).to(model.device)
            logging.debug(f'Mel spectrogram shape: {mel.shape}')
            
            options = whisper.DecodingOptions(fp16=False)
            data = whisper.decode(model, mel, options)

            prompt += data.text
            full_text += data.text

            segment_start = segment_end
            segment_end += segment_length * 1000
            i += 1

        return jsonify({'full_text': full_text}), 200

    except Exception as e:
        error_message = 'Error occurred: ' + str(e)
        logging.error(error_message)
        response = jsonify({'error': error_message})
        response.status_code = 400  # Set the status code to indicate a client error
        return response

if __name__ == '__main__':
    app.run(debug=True)
