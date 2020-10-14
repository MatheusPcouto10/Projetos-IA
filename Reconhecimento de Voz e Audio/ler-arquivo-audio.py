# Comando para instalar as bibliotecas no terminal como administrador
# pip install pipwin
# pipwin install pyaudio

import speech_recognition as sr
from pydub import AudioSegment
    
with sr.AudioFile('audio.wav') as source:
     arquivo = sr.Recognizer()

     audio = arquivo.record(source)
     
try:
        
     # Passa a variável para a API do Google
     frase = arquivo.recognize_google(audio,language='pt-BR')
     
     print(frase)
        
#Se nao reconheceu, exibe a mensagem
except sr.UnkownValueError:
     print("Não entendi")
        

