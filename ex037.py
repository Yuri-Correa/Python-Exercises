n = int(input('Digite um número inteiro: '))
print('''Escolha para qual base quer fazer a conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
e = int(input('Você escolheu: '))
if e == 1:
    print('{} em Binário é {}'.format(n, bin(n)[2:]))
elif e == 2:
    print('{} em Octal é {}'.format(n, oct(n)[2:]))
elif e == 3:
    print('{} em Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção não válida')