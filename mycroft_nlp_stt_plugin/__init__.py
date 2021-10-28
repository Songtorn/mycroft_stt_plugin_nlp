#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import requests 
import base64 
from speech_service import Speech_Service
from mycroft.stt import STT

ss = Speech_Service()

class nlpSTTPlugin(STT):
    def execute(audio, language=None):
        prediction = ss.predict(audio)
        return prediction