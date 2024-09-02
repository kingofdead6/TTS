from flask import Flask, request, send_file
import pyttsx3
from pydub import AudioSegment
import time

app = Flask(__name__)
engine = pyttsx3.init()

def save_speech_to_file(text):
    timestamp = int(time.time())  # Use the current timestamp for a unique filename
    filename = f'output_{timestamp}.mp3'
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.save_to_file(text, filename)
    engine.runAndWait()

    # Convert to WAV format
    sound = AudioSegment.from_file(filename)
    output_wav = f'output_{timestamp}.wav'
    sound.export(output_wav, format='wav')

    return output_wav

@app.route("/convert", methods=['POST'])
def convert_text_to_speech():
    text = request.form.get('text')
    wav_file = save_speech_to_file(text)
    return send_file(wav_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
