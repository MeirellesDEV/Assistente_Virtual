import pyttsx3 as py
import datetime as dt
import speech_recognition as sr
import os
import openai as op

texto_fala = py.init()

#variáveis de controle
text_mode = False #modo texto, se for verdadeiro, irá alternar a fala do microfone para modo de teclado
bot_name = 'bacaxinho' #nome do bot

#funcoes de configuração

def falar(audio):

    print(bot_name+': '+audio) #print do que o robo falar, para funções de debug


    rate = texto_fala.getProperty('rate') 
    texto_fala.setProperty(rate, 999)

    volume = texto_fala.getProperty('volume')                             
    texto_fala.setProperty(volume, 1.0)

    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[0].id)

    texto_fala.say(audio)
    texto_fala.runAndWait()

def textMode():
    global text_mode

    text_mode = not text_mode

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

def openai(comando):
    
    op.api_key = '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'

    model_engine = 'text-davinci-003'

    while True:
        #comando = microfone().lower()

        prompt = comando

        completion = op.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens = 1024,
            temperature = 0.5
        )

        response = completion.choices[0].text
        falar(response)
        break;
        #print(response)

        if 'sair' in prompt:
            break

def searchKey(dc, keywords, comando):

    for i in keywords:
        if i in comando: return keywords.index(i)
    
    return -1

def endapp():
    falar('até a próxima')
    exit()

#funcoes de comandos

def tempo():
    Tempo = dt.datetime.now().strftime("%I:%M")
    falar("Agora são: " + Tempo)

def data():
    meses = {'1':'janeiro','2':'fevereiro','3':'março','4':'abril','5':'maio','6':'junho','7':'julho','8':'agosto','9':'setembro','10':'outubro','11':'novembro','12':'dezembro'}
    ano = str(dt.datetime.now().year)
    mes = str(dt.datetime.now().month)
    dia = str(dt.datetime.now().day)
    
    falar('hoje é '+dia + ' de ' + meses[mes] + ' de ' + ano)

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

def comoestou():
    falar('Estou bem se você estiver bem meu mestre')
    falar('O que eu posso fazer para satisfaze-lo, mestre')

def navegador():
    os.system("start Chrome.exe")

def melhortime():
    falar('O melhor time certamente é o corinthians')

def quemsoueu():
     falar('Eu sou o '+ bot_name +' e é um prazer em conhecer você')


#variáveis de comandos
DICT_COMMANDS = {'como você está':comoestou, 'hora':tempo, 'data':data, 'dia é hoje':data, 'navegador':navegador, 'melhor time':melhortime, 'modo texto':textMode, 'modo fala':textMode, 'quem é você':quemsoueu, 'finalizar':endapp}

KEYWORDS = list(DICT_COMMANDS.keys())

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
        

        if searchKey(DICT_COMMANDS,KEYWORDS,comando) != -1 :
            #executando a função
            DICT_COMMANDS[KEYWORDS[searchKey(DICT_COMMANDS,KEYWORDS,comando)]]()
        else:
            openai(comando)
        