import funcoes as fc

# variáveis de comandos
AWAKE_COMMANDS = ['bacaxinho', 'abacaxi', 'cachinho', 'cachimbo', 'ximbinha',
                  'maluco', 'acorda porra', 'zé ruela', 'cabeça de lata']

if __name__ == "__main__":

    # loop principal
    while True:

        print('Aguardando chamada...')
        # aguardando chamada
        comando = fc.recebeInput()
        if fc.chamou(AWAKE_COMMANDS, comando):
            ultimoSentimento = fc.ultimoSentimento()
            fc.saudacao()
            fc.awake()

            id = '9'

        # ao chamar
        while fc.acordado:
            print("Escutando...")

            # recebendo o input
            comando = fc.recebeInput()

            # função que salva o sentimento no banco
            fc.analisarFrase(comando, id)

            #função que analisa a melhro resposta
            fc.analisar_input(comando, id)
