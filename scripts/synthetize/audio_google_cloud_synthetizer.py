from google.cloud import texttospeech

def initialize():
    global client, voice, audio_config
    client = texttospeech.TextToSpeechClient()
    voice = texttospeech.VoiceSelectionParams(
        language_code="pt", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

def synthetize(word, output_file):
    SSML = \
        '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="pt-BR">' + \
            '<prosody rate="medium">' + \
                '<phoneme alphabet="ipa" ph="'+word['ipa']+'">'+word['hr']+'</phoneme>.'+ \
            '</prosody>'+ \
        '</speak>'
    synthesis_input = texttospeech.SynthesisInput(ssml=SSML)
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file ' + output_file)

if __name__ == '__main__':
    import os
    from ipa import Words
    folder_name = 'ipa'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    initialize()
    synthetize({'ipa': "ˌna.fɛ'", 'hr': 'nafe'}, 'ipa/bafe.wav')
    # for word in Words:
    #     synthetize(word, 'ipa/' + word['hr'] + '.wav')