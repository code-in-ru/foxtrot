from Speech_Recognition import speech_recognizer
text = speech_recognizer.SpeechToText('Speech_Recognition/speech_examples/Отгорел нулевой провод.wav')
print(text.recognize())
