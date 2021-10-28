NLP STT

This project is based on:
https://github.com/scg-wedo/nlp-speech-to-text

You will need to download NLU models download

Download Models:
<br />
Microfot Team:
https://teams.microsoft.com/_#/files/General?threadId=19%3A25445bc037cb4beea185b05dc37552a3%40thread.tacv2&ctx=channel&context=speech-to-text-models&rootfolder=%252Fsites%252FDO-DigitalLabs779%252FShared%2520Documents%252FGeneral%252Fspeech-to-text-models

AWS S3:
https://s3.console.aws.amazon.com/s3/buckets/scg-dolab-dev-nlp-speech-to-text?region=ap-southeast-1&tab=objects


Project Structure:
<br />
![alt text](https://github.com/scg-wedo/mycroft_stt_plugin_nlp/blob/master/projectStructure.png?raw=true)

Installation:
<br />
cd ~/mycroft-core       
source venv-activate.sh  
mkdir plugin
cd plugin
git clone https://github.com/scg-wedo/mycroft_stt_plugin_nlp.git
pip install -e .
cd ~/mycroft-core  
mycroft-config edit user

ADD stt on user config:
<br />
```javascript
  "stt": {
    "module": "nlp_stt_plugin"
  }
```
<br />
[Ctrl + X]

./start-mycroft.sh debug


-Now try to speak with Mycroft