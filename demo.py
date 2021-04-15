# -*- coding: utf-8 -*-
#
# Time-stamp: <Tuesday 2020-07-07 16:28:31 AEST Graham Williams>
#
# Copyright (c) Togaware Pty Ltd. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Azure Cognitive Services Speech to Text Quick Start

from mlhub.pkg import azkey, mlask, mlcat

mlcat("Speech Services", """\
Welcome to a demo of the pre-built models for Speech provided
through Azure's Cognitive Services. The Speech cloud service 
supports speech to text, text to speech, speech translation and 
Speaker Recognition capabilities.
""")

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

# Import the required libraries.

import os
import sys
from translate import translate_speech_to_text
from recognise import recognise
import azure.cognitiveservices.speech as speechsdk

# ----------------------------------------------------------------------
# Request subscription key and location from user.
# ----------------------------------------------------------------------

SERVICE = "Speech"
KEY_FILE = os.path.join(os.getcwd(), "private.txt")

key, location = azkey(KEY_FILE, SERVICE, connect="location")

# -----------------------------------------------------------------------
# Set up a speech recognizer and synthesizer.
# -----------------------------------------------------------------------

# Following is the code that does the actual work, creating an
# instance of a speech config with the specified subscription key and
# service region, then creating a recognizer with the given settings,
# and then performing recognition. recognize_once() returns when the
# first utterance has been recognized, so it is suitable only for
# single shot recognition like command or query. For long-running
# recognition, use start_continuous_recognition() instead, or if you
# want to run recognition in a non-blocking manner, use
# recognize_once_async().

speech_config = speechsdk.SpeechConfig(subscription=key, region=location)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# -----------------------------------------------------------------------
# Transcribe some spoken words.
# -----------------------------------------------------------------------

mlask(end="\n")

mlcat("Speech to Text", """\
Now say something, it will transcribe into text. """)

mlask(end=True, prompt="Press Enter and then say something")

result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))

mlask(end="\n")

# -----------------------------------------------------------------------
# Request text from console input.
# -----------------------------------------------------------------------

mlcat("Text to Speech", """\
Now type text to be spoken. When Enter is pressed you will hear the result.
""")

text = input()

# Synthesize the text to speech. When the following line is run expect
# to hear the synthesized speech.

result = speech_synthesizer.speak_text_async(text).get()

# -----------------------------------------------------------------------
# Translate language to other language
# -----------------------------------------------------------------------

mlask(begin="\n")

mlcat("Speech Translation", """\
This part is to translate English to other language. Now please speak English. 
This speech service will translate it to French.
""")

mlask()
translate_speech_to_text("en-US", "fr")

# -----------------------------------------------------------------------
# Confirming that the speaker matches a known, or enrolled voice
# -----------------------------------------------------------------------

mlask(begin="\n")
mlcat("Speaker Recognition", """\
This part is the act of confirming that a speaker matches a enrolled voice. 
Now you will hear four audios. The first three will be the sample audios, 
and the fourth one will be the audio that needs to compare against them.
""")

first = os.path.join(os.getcwd(), "audio.wav")
second = os.path.join(os.getcwd(), "audio1.wav")
third = os.path.join(os.getcwd(), "audio2.wav")

# Play the first video
mlask(begin="\n")
mlcat("The first sample audio...", """""")
os.system(f'aplay {first} >/dev/null 2>&1')

# Play the second video
mlcat("The second sample audio...", """""")
os.system(f'aplay {second} >/dev/null 2>&1')

# Play the third video
mlcat("The third sample audio...", """""")
os.system(f'aplay {third} >/dev/null 2>&1')

# Play the fourth video

mlcat("The fourth audio that needs to identify...", """""")
os.system(f'aplay {fourth} >/dev/null 2>&1')


mlcat("Get the result", """\
Now, we will insert the first three examples into our recognition system, 
and use these samples to verify the fourth audio by its unique voice 
characteristics. 
""")

mlask(begin="\n")
recognise([first, second, third], fourth)







