#!/usr/bin/python3
from googletrans import Translator

translator = Translator()

res = translator.translate("A Római Birodalom (latinul Imperium Romanum) az ókori Róma által létrehozott államalakulat volt a Földközi-tenger medencéjében.", dest='fr')
print(res.text)
