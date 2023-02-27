import pyttsx3 as py
import datetime as dt
import speech_recognition as sr
import os
import webbrowser as wb
import openai as op

import spotipy
from spotipy.oauth2 import SpotifyOAuth

texto_fala = py.init()

<<<<<<< Updated upstream
#variáveis de controle
text_mode = False #modo texto, se for verdadeiro, irá alternar a fala do microfone para modo de teclado

bot_name = 'bacaxinho' #nome do bot


def falar(audio):
    print(audio) #print do que o robo falar, para funções de debug
=======
# variáveis de controle
# modo texto, se for verdadeiro, irá alternar a fala do microfone para modo de teclado
text_mode = True
bot_name = 'bacaxinho'  # nome do bot

# funcoes de configuração


def falar(audio):
>>>>>>> Stashed changes

    # print do que o robo falar, para funções de debug
    print(bot_name+': '+audio)

    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty(rate, 60)

    volume = texto_fala.getProperty('volume')
    texto_fala.setProperty(volume, 1.0)

    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[0].id)

    texto_fala.say(audio)
    texto_fala.runAndWait()


<<<<<<< Updated upstream
def tempo():
    Tempo = dt.datetime.now().strftime("%I:%M")
    falar("Agora são: " + Tempo)

def data():
    meses = {'1':'janeiro','2':'fevereiro','3':'março','4':'abril','5':'maio','6':'junho','7':'julho','8':'agosto','9':'setembro','10':'outubro','11':'novembro','12':'dezembro'}
    ano = str(dt.datetime.now().year)
    mes = str(dt.datetime.now().month)
    dia = str(dt.datetime.now().day)

    falar("A data atual é: ")

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
=======
def textMode():
>>>>>>> Stashed changes
    global text_mode
    text_mode = condition



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

<<<<<<< Updated upstream

def openia():
    
    #op.api_key = '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'
=======
>>>>>>> Stashed changes

def openia(fala):
    falar('Pesquisa: '+fala)
    # op.api_key = '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'

    #model_engine = 'text-davinci-003'

    # while True:
    #     # comando = microfone().lower()

    #     prompt = fala

    #     completion = op.Completion.create(
    #         engine=model_engine,
    #         prompt=prompt,
    #         max_tokens=1024,
    #         temperature=0.5
    #     )

    #     response = completion.choices[0].text
    #     falar(response)
    #     # print(response)

    #     if 'sair' in prompt:
    #         break


<<<<<<< Updated upstream
=======
def searchKey(dc, keywords, comando):

    for i in keywords:
        if i in comando:
            return keywords.index(i)

    return -1


def ouvir():
    listener = sr.Recognizer()
    sr.Microphone.list_microphone_names()

    try:
        with sr.Microphone(device_index=1) as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='pt-PT')
            print(command)
            return command
    except:
        return 'No Sound'


def spotify():

    os.environ['SPOTIPY_CLIENT_ID'] = '<d42fde4f8111483087e47122e353b9f2>'
    os.environ['SPOTIPY_CLIENT_SECRET'] = '0e56ae6b8c45442588a032688690732e'
    os.environ['SPOTIPY_REDIRECT_URI'] = 'https://example.com/callback'

    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

    engine = py.init()
    engine.runAndWait()

    while True:
        falar('Qual musica você deseja campeão?')

        command = microfone()

        if 'sair' in command:
            break
        else:
            results = sp.search(command, 1, 0, "track")

            nome_artista = results['tracks']['items'][0]['artists'][0]['name']
            nome_musica = results['tracks']['items'][0]['name']
            track_uri = results['tracks']['items'][0]['uri']

            engine.say(f'Tocando {nome_musica} by {nome_artista}')
            engine.runAndWait()

            sp.start_playback(uris=[track_uri])

    


def endapp():
    falar('até a próxima')
    exit()

# funcoes de comandos


def tempo():
    Tempo = dt.datetime.now().strftime("%I:%M")
    falar("Agora são: " + Tempo)


def data():
    meses = {'1': 'janeiro', '2': 'fevereiro', '3': 'março', '4': 'abril', '5': 'maio', '6': 'junho',
             '7': 'julho', '8': 'agosto', '9': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'}
    ano = str(dt.datetime.now().year)
    mes = str(dt.datetime.now().month)
    dia = str(dt.datetime.now().day)

    falar("A data atual é: ")
    falar(dia + 'de ' + meses[mes] + 'de ' + ano)


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
    falar('Eu sou o ' + bot_name + ' e é um prazer em conhecer você')


def codigofonte():
    wb.open('https://github.com/MeirellesDEV/Assistente_Virtual')


# variáveis de comandos
DICT_COMMANDS = {'como você está': comoestou, 'hora': tempo, 'data': data, 'dia é hoje': data,'navegador': navegador, 'melhor time': melhortime, 'modo texto': textMode, 'modo fala': textMode, 'quem é você': quemsoueu, 'código fonte': codigofonte, 'finalizar': endapp, '': spotify}

KEYWORDS = list(DICT_COMMANDS.keys())

>>>>>>> Stashed changes
if __name__ == "__main__":
    saudacao()

    while True:

        print("Escutando...")

        # recebendo o input
        if text_mode is True:
            print('digite alguma coisa: ')
            comando = input('>> ')
        else:
            comando = microfone().lower()
<<<<<<< Updated upstream

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

        elif 'pesquisar por' in comando:
            openia()

        elif 'finalizar' in comando:
            falar('até a próxima!')
            break
=======

        if searchKey(DICT_COMMANDS, KEYWORDS, comando) != -1:DICT_COMMANDS[KEYWORDS[searchKey(DICT_COMMANDS, KEYWORDS, comando)]]()

        else:
            openia(comando)
>>>>>>> Stashed changes
