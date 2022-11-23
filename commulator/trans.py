#!/usr/bin/python3
from googletrans import Translator

text = """This Evaluation Quiz is to support your growth towards a software engineering role; we know how difficult the upcoming road will be, and we want to ensure you are ready for its challenges. The data has shown when students comprehend below a certain threshold they do not experience success after the program; this accountability is preventative to make sure we can help you get any help you may need. We are here to help!
"""

translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.kr',
])

dt1 = translator.translate(text, dest='fr')
name = dt1.text
print(name)
# text = translator.detect(name)
# print(text)
