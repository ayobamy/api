#!/usr/bin/python3
from googletrans import Translator

text = """This Evaluation Quiz is to support your growth towards a software engineering role; we know how difficult the upcoming road will be, and we want to ensure you are ready for its challenges. The data has shown when students comprehend below a certain threshold they do not experience success after the program; this accountability is preventative to make sure we can help you get any help you may need. We are here to help!

Once you have started the quiz, you may not click out, search on Google, open terminal, etc.

Failure to stay within the exam window will reflect your final score.

If you complete the quiz sooner than to be anticipated, that is acceptable. The quiz, however, cannot be paused once you have started.

You are not allowed to ask peers for answers during the exam period. You can, however, use paper and pen to organize your thoughts.

If you take the exam onsite during the specified exam time , you will receive 100% point potential.

If you take the exam offsite during the specified time or at any time other than the specified exam time (onsite or offsite), you will receive 65% point potential."""

translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.kr',
])

dt1 = translator.translate(text, dest='fr')
name = dt1.text
print(name)
# text = translator.detect(name)
# print(text)
