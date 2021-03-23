# pip install moviepy

import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

# Retirando o texto de uma videoaula
aula = mp.VideoFileClip('aula.mp4').subclip(0,120)
aula.audio.write_audiofile('aula.wav')

with sr.AudioFile('aula.wav') as source:
     arquivo = sr.Recognizer()

     audio = arquivo.record(source)   

     # Passa a variável para a API do Google
     frase = arquivo.recognize_google(audio,language='pt-BR')
     
     
print("\n Texto da VideoAula: ")
print(frase)

# Separa o texto da ementa em sentenças/períodos
periodos = sent_tokenize(frase)
print("\n Texto separado em Períodos: ")
print(periodos)
print("\n")

# Separa o texto da ementa em palavras e retira as stopwords e pontuações
palavras = word_tokenize(frase)
palavras = [word.lower() for word in palavras if word.isalpha()]
periodo_puro = [word for word in palavras if word not in stopwords.words('portuguese')]
print("Texto com StopWords e pontuações retirados: ")
print(periodo_puro)


