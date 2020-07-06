from googletrans import Translator

class Tradutor():
	def __init__(self):
		print('traduzindo...')


	def traduza(palavra, lang):
		translator = Translator()
		p = palavra
		print('p',p)
		frase =(translator.translate(f'{p}', dest=lang))
		print('frase=',frase.text)
		return frase.text


