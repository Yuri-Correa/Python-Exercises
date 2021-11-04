a = int(input('Digite um número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a >b:
    if b >c:
        print('O maior número é {} e menor é {}'.format(a, c))
    else:
        if a >c:
            print('O maior número é {} e menor é {}'.format(a, b))
        else:
            print('O maior número é {} e o menor é {}'.format(c, b))
else:
    if a >c:
        print('O maior número é {} e o menor é {}'.format(b, c))
    else:
        if b >c:
            print('O maior número é {} e o menor é {}'.format(b, a))
        else:
            print(f'O maior número é {c} e o menor é {a}')