import speech_recognition as sr
import pyaudio
import wave


def record_audio(output_file, record_seconds=5, sample_rate=16000, channels=1):
    audio_format = pyaudio.paInt16
    chunk = 1024

    audio = pyaudio.PyAudio()

    stream = audio.open(format=audio_format, channels=channels,
                        rate=sample_rate, input=True,
                        frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    for _ in range(0, int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_file, "wb") as wave_file:
        wave_file.setnchannels(channels)
        wave_file.setsampwidth(audio.get_sample_size(audio_format))
        wave_file.setframerate(sample_rate)
        wave_file.writeframes(b''.join(frames))


output_file = "output.wav"
record_seconds = 5
record_audio(output_file, record_seconds)


r = sr.Recognizer()

with sr.AudioFile('output.wav') as source:
    audio_text = r.listen(source)

    try:
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
         print('Sorry.. run again...')

