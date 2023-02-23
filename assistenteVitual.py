import pyttsx3 as py
import datetime as dt
import speech_recognition as sr
import os

texto_fala = py.init()


def falar(audio):

    texto_fala.setProperty("rate", 155)
    texto_fala.say(audio)
    texto_fala.runAndWait()

# falar("isso ae")


def tempo():
    Tempo = dt.datetime.now().strftime("%I:%M")
    falar("Agora são: " + Tempo)

# tempo()


def data():
    ano = str(dt.datetime.now().year)
    mes = str(dt.datetime.now().month)
    dia = str(dt.datetime.now().day)

    falar("A data atual é: ")
    falar(dia + " do " + mes + " de " + ano)

# data()


def saudacao():

    falar("Olá poderossimo Mago. Bem vindo de volta!")
    # tempo()
    # data()

    # hora = dt.datetime.now().hour

    # if hora >= 6 and hora <= 12:
    #     falar("Bom dia o mais pika dos magos!")
    # elif hora > 12 and hora <= 18:
    #     falar("Boa tarde meu querido poderoso mestre!")
    # else:
    #     falar("Boa noite mestre-chan!")

    falar("Bacaxinho a sua disposição! Lance a braba!")

# saudacao()


def microfone():
    r = sr.Recognizer()

    with sr.Microphone() as mic:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)

    try:
        print("Reconhecendo...")
        comando = r.recognize_google(audio, language='pt-BR')
        print(comando)

    except Exception as e:
        print(e)
        falar("Por favor repita, não te escutei!")

        return "None"

    return comando

# microfone()


if __name__ == "__main__":
    saudacao()

    while True:
        print("Escutando...")

        comando = microfone().lower()

        if 'como você está' in comando:
            falar('Estou bem se você estiver bem meu mestre')
            falar('O que eu posso fazer para satisfaze-lo, mestre')

        elif 'hora' in comando:
            tempo()

        elif 'data' in comando:
            data()

        elif 'navegador' in comando:
            os.system("start Chrome.exe")

        elif 'finalizar' in comando:
            falar('Estamos finalizando por aqui')
            break
