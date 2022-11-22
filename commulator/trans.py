#!/usr/bin/python3
from googletrans import Translator

text = "The token is based on a seed which is updated once per hour and on the text that will be translated. Both are combined - by some strange math - in order to generate a final token (e.g. 744915.856682) which is used by the API to validate the request."

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

dt1 = translator.translate(text, dest='yo')
name = dt1.text
print(name)
# text = translator.detect(name)
# print(text)
