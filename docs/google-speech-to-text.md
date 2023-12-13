Sample SSML (https://cloud.google.com/text-to-speech/docs/ssml) to synthetize two words with one second between them:

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="pt-BR">
<phoneme alphabet="ipa" ph="ˈsa.ti">sáti</phoneme>.
<break time='1s'/>
<phoneme alphabet="ipa" ph="ˈsa.ti">sáti</phoneme>.
</speak>
```

Console to synthetize up to 5000 bytes:

https://console.cloud.google.com/speech/text-to-speech