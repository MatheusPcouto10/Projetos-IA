# Comando para instalar as bibliotecas no terminal como administrador
# pip install pipwin
# pipwin install pyaudio

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#Cria o arquivo de audio
def cria_audio(audio):

    tts = gTTS(audio,lang='pt-br')

    tts.save('audio.mp3')

    playsound('audio.mp3')

def ouvir_microfone():

    #Ativa o microfone
    microfone = sr.Recognizer()
    
    #Usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para a API do Google
        frase = microfone.recognize_google(audio,language='pt-BR')
     
        print("Você disse: " + frase)
        
    #Se nao reconheceu, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase

frase = ouvir_microfone()
cria_audio(frase)    