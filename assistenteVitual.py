import pyttsx3 as py
import datetime as dt
import speech_recognition as sr
import os

texto_fala = py.init()

#variáveis de controle
text_mode = False #modo texto, se for verdadeiro, irá alternar a fala do microfone para modo de teclado

bot_name = 'bacaxinho' #nome do bot


def falar(audio):
    print(audio) #print do que o robo falar, para funções de debug


    texto_fala.setProperty("rate", 155)
    texto_fala.say(audio)
    texto_fala.runAndWait()

def tempo():
    Tempo = dt.datetime.now().strftime("%I:%M")
    falar("Agora são: " + Tempo)

def data():
    meses = {'1':'janeiro','2':'fevereiro','3':'março','4':'abril','5':'maio','6':'junho','7':'julho','8':'agosto','9':'setembro','10':'outubro','11':'novembro','12':'dezembro'}
    ano = str(dt.datetime.now().year)
    mes = str(dt.datetime.now().month)
    dia = str(dt.datetime.now().day)

    falar("A data atual é: ")
    falar(dia + " de " + meses[mes] + " de " + ano)

def saudacao():

    falar("Olá poderosíssimo Mago. Bem vindo de volta!")
    # tempo()
    # data()

    # hora = dt.datetime.now().hour

    # if hora >= 6 and hora <= 12:
    #     falar("Bom dia o mais pika dos magos!")
    # elif hora > 12 and hora <= 18:
    #     falar("Boa tarde meu querido poderoso mestre!")
    # else:
    #     falar("Boa noite mestre-chan!")

    falar(bot_name+" a sua disposição! Lance a braba!")

def textMode(condition):
    global text_mode
    text_mode = condition


#mic settings
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



if __name__ == "__main__":
    saudacao()

    while True:
        print("Escutando...")

        #recebendo o input
        if text_mode is True:
            print('digite alguma coisa: ')
            comando = input('>> ')
        else:
            comando = microfone().lower()

        #comando de saudação
        if 'como você está' in comando: 
            falar('Estou bem se você estiver bem meu mestre')
            falar('O que eu posso fazer para satisfaze-lo, mestre')

        elif 'hora' in comando: #comando que fala aa hora
            tempo()

        elif 'data' in comando or 'dia é hoje' in comando: #comando que diz a data
            data()

        elif 'navegador' in comando: #comando que abre o navegador
            os.system("start Chrome.exe")
        
        elif 'melhor time' in comando:
            falar('O melhor time certamente é o corinthians')
        
        elif 'modo texto' in comando:
            falar('iniciando modo texto')
            textMode(True)
        
        elif 'modo fala' in comando:
            falar('iniciando modo de fala')
            textMode(False)
            
        elif 'bom dia' in comando:
            falar('bom dia campeão')

        elif 'quem é você' in comando:
            falar('Eu sou o '+ bot_name +' e é um prazer em conhecer você')

        elif 'finalizar' in comando:
            falar('até a próxima!')
            break
