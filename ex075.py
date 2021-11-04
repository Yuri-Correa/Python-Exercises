while True:
    cont = 0
    a = int(input('Digite um número: ' ))
    b = int(input('Digite outro número: '))
    c = int(input('Digite mais um número: '))
    d = int(input('Agora digite o último número: '))
    t = a, b, c, d
    if a != 0 or b != 0 or c != 0 or d != 0:
        print('=' * 40)
        print(f'Você digitou os números {t}')
        print(f'O número 9 apareceu {t.count(9)} vezes')
        a = str(3 in t)
        if a == 'True':
            print(f'O número 3 apareceu na {(t.index(3)+1)}ª posição')
        else:
            print(f'O número 3 não apareceu nenhuma vez!!')
        print('Os valores pares digitados: ', end='')
        for n in t:
            if n % 2 == 0:
                print(n, end=' ')
                cont += 1
            elif cont == 0:
                print('Nenhum valor par digitado!', end=' ')
                cont += 1
        print('\n', '=' * 40)
    elif a == 0 and b == 0 and c == 0 and d == 0:
        break
print('Fim')