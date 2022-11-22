from googletrans import Translator

translator = Translator()

dt1 = translator.translate("Vysoké Tatry sú najvyššie pohorie na Slovensku a v Poľsku a sú zároveň jediným horstvom v týchto štátoch s alpským charakterom.", dest='en')
print(dt1.text)

dt2 = translator.translate("A Római Birodalom (latinul Imperium Romanum) az ókori Róma által létrehozott államalakulat volt a Földközi-tenger medencéjében", dest='yo')
print(dt2.text)
