nome_usuario = input('Digita seu nome: ')
idade_usuario = input('Digita sua idade: ')

if nome_usuario and idade_usuario :
    print(f'Seu nome é: {nome_usuario}')
    print(f'Seu nome invertido é {nome_usuario[::-1]}')
    if ' ' in nome_usuario:
        print('Seu nome tem espaço.')
    else:
        print('Seu nome não tem espaço.')    

    print(f'Seu nome tem {len(nome_usuario)} letras.')
    print(f'A primeira letra do seu nome é: {nome_usuario[0]}')
    print(f'A ultima letra do seu nome é: {nome_usuario[-1]}')
else:
    print('Desculpe, você deixou algum campo vazil!')

