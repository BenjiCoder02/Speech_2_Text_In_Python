import os
import speech_recognition as sr
from mutagen.wave import WAVE
from pydub import AudioSegment
from pydub.silence import split_on_silence
import shutil
import sys

file_name = sys.argv[1]

command2mp3 = f'ffmpeg -i ./Clips/{file_name}.mp4 {file_name}.mp3'
command2wav = f'ffmpeg -i {sys.argv[1]}.mp3 {sys.argv[1]}.wav'

os.system(command2mp3)
os.system(command2wav)

audioSample = WAVE(str(file_name + '.wav'))

r = sr.Recognizer()

def get_large_audio_transcript(path):
    full_audio = AudioSegment.from_wav(path)

    chunks = split_on_silence(full_audio, min_silence_len=300, silence_thresh=full_audio.dBFS-14, keep_silence=500)

    folder_name = "audio-chunks"
    shutil.rmtree(folder_name)

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""

    for i, audio_chunk in enumerate(chunks, start=1):

        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")

        with sr.AudioFile(chunk_filename) as source:
            audioSampleChunk = WAVE(chunk_filename)
            audioSample_info = audioSampleChunk.info
            duration_in_s = audioSample_info.length
            audio_listened = r.record(source, duration_in_s)

            try:
                text = r.recognize_google(audio_listened, None, 'en-US', 0, False)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
                
    return whole_text

path = f"{file_name}.wav"

print(get_large_audio_transcript(path))
