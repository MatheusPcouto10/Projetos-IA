# Comando para instalar as bibliotecas no terminal como administrador
# pip install pipwin
# pipwin install pyaudio


from gtts import gTTS
from playsound import playsound

#Cria o arquivo de audio
def cria_audio(audio):

    tts = gTTS(audio,lang='pt-br')

    tts.save('audio.mp3')

    playsound('audio.mp3')

# Le o que o usuario digita
def ler_frase():

    frase = input("digite o que deseja falar: ")
        
    return frase

audio = ler_frase()
cria_audio(audio)    