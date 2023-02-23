import openai as op

op.api_key = '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'

model_engine = 'text-davinci-003'

while True:
    prompt = input('Escreva algo: ')

    completion = op.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        temperature = 0.5
    )

    response = completion.choices[0].text
    print(response)

    # saida = input('Você deseja sair do chat?')
    # if saida == 'sim':
    #     break