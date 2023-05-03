import funcoes as fc

# variáveis de comandos

AWAKE_COMMANDS = ['bacaxinho', 'abacaxi', 'cachinho', 'cachimbo', 'ximbinha',
                  'maluco', 'acorda porra', 'zé ruela', 'cabeça de lata']

# KEYWORDS = list(DICT_COMMANDS.keys())

if __name__ == "__main__":

    # loop principal
    while True:

        print('Aguardando chamada...')
        # aguardando chamada
        comando = fc.recebeInput()
        if fc.chamou(AWAKE_COMMANDS, comando):
            fc.saudacao()
            fc.awake()

        # ao chamar
        while fc.acordado:
            print("Escutando...")

            # recebendo o input
            comando = fc.recebeInput()

            # função que salva o sentimento no banco
            # fc.analisarFrase(comando)

            #função que analisa a melhro resposta
            fc.analisar_input(comando)

            # if fc.searchKey(DICT_COMMANDS, KEYWORDS, comando) != -1:
            #     # executando a função
            #     DICT_COMMANDS[KEYWORDS[fc.searchKey(
            #         DICT_COMMANDS, KEYWORDS, comando)]]()

            # elif 'youtube' in comando:
            #     fc.youtube(comando)
            # elif 'google' in comando:
            #     fc.google(comando)
            # elif 'como fala' in comando:
            #     fc.tradutor(comando)
            # else:
            #     fc.openia(comando)
