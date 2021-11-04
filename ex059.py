a = float(input('Digite o 1 número: '))
b = float(input('Digite o 2 número: '))
e = 0
while e != 5:
    e = int(input('''O que deseja fazer:
    [ 1 ] - SOMAR
    [ 2 ] - MULTIPLICAR
    [ 3 ] - MAIOR
    [ 4 ] - NOVOS NÚMEROS
    [ 5 ] - SAIR DO PROGRAMA
    OPÇÃO ESCOLHIDA: '''))
    if e == 1:
        print('\nA soma dos números {:.2f} e {:.2f} é igual a: {:.2f}!\n'.format(a, b, a+b))
    elif e == 2:
        print('\nO produto dos números {:.2f} e {:.2f} é igual a: {:.2f}!\n'.format(a, b, a*b))
    elif e == 3:
        if a > b:
            print('\nO número {:.2f} é maior que o número {:.2f}!\n'.format(a, b))
        elif b > a:
            print('\nO número {:.2f} é maior que o número {:.2f}!\n'.format(b, a))
        else:
            print('\nOs números {:.2f} e {:.2f} são iguais!\n'.format(a, b))
    elif e == 4:
        a = float(input('\n1 - Digite o novo valor: '))
        b = float(input('2 - Digite o novo valor: '))
print('FIM')