from gtts import gTTS
import os
import convert

def text_to_speech(text, lang='en', output_file='output.wav'):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    print(f"Saved the speech to {output_file}")

if __name__ == "__main__":
    text = convert.text
    text_to_speech(text)
