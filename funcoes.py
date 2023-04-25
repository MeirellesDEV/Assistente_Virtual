import pyttsx3 as py
import datetime as dt
import speech_recognition as sr
import os
import webbrowser as wb
import openai as op

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import wikipedia as wk

from googletrans import Translator


texto_fala = py.init()

# variáveis de controle
# modo texto, se for verdadeiro, irá alternar a fala do microfone para modo de teclado
text_mode = True
acordado = False
bot_name = 'bacaxinho'  # nome do bot

# funcoes de configuração
def falar(audio):

    # print do que o robo falar, para funções de debug
    print(bot_name+': ' + audio)

    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty(rate, 999)

    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty(rate, 120)

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

def openia(fala):

    falar('Pesquisa por OPENAI desativada por enquanto...')
    # op.api_key = 'token'

    # model_engine = 'text-davinci-003'

    # while True:
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

def searchKey(dc, keywords, comando):

    for i in keywords:
        if i in comando:
            return keywords.index(i)

    return -1

def ouvir():
    print('escutando microfone...')
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

    os.environ['SPOTIPY_CLIENT_ID'] = 'token'
    os.environ['SPOTIPY_CLIENT_SECRET'] = 'token'
    os.environ['SPOTIPY_REDIRECT_URI'] = 'redirect'

    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

    engine = py.init()
    engine.runAndWait()

    falar('Qual musica você deseja campeão?')

    command = recebeInput()

    if 'pausar' in command:
        sp.pause_playback()
    elif 'continue' in command:
        sp.start_playback()
    elif 'mudar volume' in command:
        volume = int(command.lower().replace('mudar volume', '').strip())
        sp.volume(volume)
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

def apresentacao():
    falar('Digas, o Pinaculo do Design')
    wb.open('https://github.com/RodrigoTheDev')

    falar('Meirelles, a Sacerdotisa do Front')
    wb.open('https://github.com/MeirellesDEV')

    falar('João, o Redentor das APIs')
    wb.open('https://github.com/JGsilvaDev')

def wikipedia():
    wikipedia.set_lang("pt-BR")
    falar('O que você quer pesquisar no wikipedia?')
    s = recebeInput()
    l = wikipedia.search(str(s))

    for i in l:
        falar(wikipedia.summary(i, sentences=1))

def google(comando):
    search_term = comando.replace("google", "")
    url = 'https//www.google.com/search?q=' + search_term
    wb.get().open(url)
    falar("Aqui está o que você pesquisou" + search_term)

def youtube(comando):
    search_term = comando.replace("youtube", "")
    url = 'https//www.youtube.com/results?search_query=' + search_term
    wb.get().open(url)
    falar("Aqui está o que você pesquisou" + search_term)

def searchKey(dc, keywords, comando):

    for i in keywords:
        if i in comando:
            return keywords.index(i)

    return -1

def chamou(list, command):
    for i in list:
        if i in command:
            return True
    return False

def recebeInput():
    if text_mode is True:
        print('digite alguma coisa: ')
        comando = input('>> ')
    else:
        comando = microfone().lower()

    return comando

def awake():
    global acordado
    acordado = not acordado

def novoapelido():
    global AWAKE_COMMANDS
    falar('Como você quer me chamar a partir de hoje?')
    comando = recebeInput()

    comando.partition(' ')
    AWAKE_COMMANDS.append(comando)

    falar('Muito bem, '+comando+' foi adicionado como um novo apelido')

def novonome():
    global bot_name

    falar('como você quer que eu me chame?')

    novo_nome = recebeInput()

    bot_name = novo_nome

    falar('nome alterado com sucesso')

def listarApelidos():
    global AWAKE_COMMANDS

    falar('As pessoas me chamam de: ')
    for i in AWAKE_COMMANDS:
        falar(i)

def tradutor(fala):
    trans = Translator()

    LANGUAGES = {
        'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani',
        'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan',
        'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)',
        'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
        'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian',
        'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
        'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong',
        'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian',
        'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean',
        'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian',
        'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam','mt': 'maltese',
        'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian',
        'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi',
        'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
        'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali',
        'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil',
        'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek',
        'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba','zu': 'zulu'
    }

    txt = str(fala.replace('como fala', '').replace('em', '')).split()
    lang = txt[-1]

    idioma = str(trans.translate(lang, dest="en").text).lower()

    items = LANGUAGES.items()

    for item in items:
        if(item[1] == idioma):
            codLang = item[0]

    txt.pop()                   #retira a linguagem do array
    conteudo = ' '.join(txt)

    falar(trans.translate(conteudo, dest=codLang).text)
