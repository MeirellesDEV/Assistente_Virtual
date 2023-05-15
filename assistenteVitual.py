import funcoes as fc

if __name__ == "__main__":

    # loop principal
    while True:

        id = '9'

        # recebendo o input
        comando = fc.recebeInput()

        #pega o utlimo sentimento
        sentimento = fc.ultimoSentimento(id)

        fc.nivelSentimento(sentimento, id)

        # função que salva o sentimento no banco
        fc.analisarFrase(comando, id)

        #função que analisa a melhro resposta
        fc.analisar_input(comando)
