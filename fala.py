from gtts import gTTS

class Fala:
	def __init__(palavra):
		p = palavra
		tts = gTTS(text=palavra, lang='en')
		file = tts.save('fala.mp3')
		print('salvo')
		#return file

	def falar(palavra):
		p = palavra
		tts = gTTS(text=palavra, lang='pt')
		file = tts.save('eva.mp3')
		print('salvo')

	def fale(palavra):
		p = palavra
		tts = gTTS(text=palavra, lang='pt')
		file = tts.save('eva.wav')
		print('salvo')