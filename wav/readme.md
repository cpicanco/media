This folder contains all `*.wav` files of the COLANG and other protocols with its corresponding confection method.

For `cvcv` pseudowords, there are two human voices (Rafael e Giulia) and one robot voice (Maria).

# Robot voice synthesis

`cvcv.wav` files inside `microsoft-maria-pseudowords` are text-to-speech words synthesized using Microsoft's Speech Object Library (SAPI), with the following SSML template (for the word befo):

```xml
  Result := '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="pt-BR">' +
    '<voice name="Microsoft Maria Desktop - Portuguese(Brazil)">' +
      '<prosody rate="10%">' +
        '<phoneme alphabet="ipa" ph="bɛ.ˈfɔ">befo</phoneme>.'+
      '</prosody>'+
    '</voice>'+
  '</speak>';
```

# Human voices

`cvcv.wav` files inside `giulia-pseudowords` and `rafael-pseudowords` were recorded with:

- a cardioide condenser microphone (Arcano AM-01)
- an USB audio interface with ASIO support for cd quality and real time low latency recordings (Line 6 UX1)
- a digital audio workstation (Reaper: https://www.reaper.fm/) and
- studio like rooms, with sound attenuation 

Also, a playback track with 256 synthesized words, spaced by ~2.8 seconds, disposed in alphabetical order, guided recordings in a request-response style (synthesized word first, then spoken word).
Phonetic errors were corrected in place, restarting recordings of missed words as they occured and were noticed.
The recording session finneshed after three complete runs with all words.

After the recording session, an effect chain was applied (words.Rfx.Chain) to improve audio clarity and sound normalization.
The the track was heard 6 times and when a phonetic error was noticed it was replaced in-place by a correct phonetic copied from the recording session.
