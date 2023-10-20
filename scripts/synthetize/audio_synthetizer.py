# from gtts import gTTS
# from pydub import AudioSegment
# import io
import win32com.client

def synthetize(text, output_file):
    try:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        stream = win32com.client.Dispatch("SAPI.SpFileStream")
        stream.Open(output_file, 3)  # 3 stands for SPFileMode.SPFMCreate
        speaker.Rate = -1.0
        speaker.AudioOutputStream = stream
        speaker.Speak(text, 8) # 8 stands for SVSFIsXML
        stream.Close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Create a gTTS pronunciation for the given word and save it to the given output file
# def synthetize(word, output_file):
#     tts = gTTS(word, lang='pt', tld='com.br', slow=True)
#     audio_io = io.BytesIO()
#     tts.write_to_fp(audio_io)
#     audio_io.seek(0)
#     audio_segment = AudioSegment.from_file(audio_io)
#     audio_segment.export(output_file, format='wav')

if __name__ == '__main__':

    synthetize('<pron sym="b o - f a 1"/>', 'ipa/_test.wav')