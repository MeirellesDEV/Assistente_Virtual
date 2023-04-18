import json

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import time
time.clock = time.time

data = json.loads(open('../input/chatBot.json', 'r').read())

sentimento = 'alegria'
train = []

for row in data:
    for i in range(len(row['question'])):
        train.append(row['question'][i])

        if sentimento == 'alegria':
            train.append(row["resposta"]['alegria'])

        if sentimento == 'tristeza':
            train.append(row["resposta"]['tristeza'])

        if sentimento == 'raiva':
            train.append(row["resposta"]['raiva'])

        if sentimento == 'neutro':
            train.append(row["resposta"]['neutro'])

print(train)

chatbot = ChatBot('Bacaxinho')
trainer = ListTrainer(chatbot)
trainer.train(train)

while True:
    mensagem = input("Mande uma msg pro bot:")
    if mensagem == "parar":
        break

    if mensagem == "":
        resposta = 'Não entendi oq vc falou'
        
    resposta = chatbot.get_response(mensagem)
    print('Eu:', mensagem)
    print('Bacaxinho: ', resposta)