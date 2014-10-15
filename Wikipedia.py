# -*- coding: utf-8-*-
import random
import re
import jasperpath
import wikipedia

WORDS = ["INFO", "INFORMATION", "TELL", "ME"]

def handle(text, mic, profile):

mic.say("What do you want to know?")
topic = mic.activeListen()
sentence = wikipedia.summary(topic, sentences=2)
mic.say("Information about %s" % topic)
mic.say(sentence)

def isValid(text):
        infoBool = bool(re.search(r'\info|information|tell me\b', text, re.IGNORECASE))

        if infoBool:
                return infoBool
        else:
                return False
