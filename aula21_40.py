entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = int(input ('Digite sua senha: '))

senha_permitida = 1736


if entrada == 'E' and senha_digitada == senha_permitida:
    print('Parabens, você esta logado!')

elif entrada == 'S':
    print('Você saiu do sistema!')   
else:
    print('Você digitou a senha errada!, tente novamente')