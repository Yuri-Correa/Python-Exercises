from random import randint
from time import sleep


def sorteia(num):
    print('='*50)
    print('Sorteando os valores da lista...')
    sleep(1)
    for c in range(0, 5):
        n = randint(1, 10)
        num.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('Pronto!')
    print('='*50)


def somapar(num):
    print('=' * 50)
    soma = 0
    print('A soma dos números pares de ', end='')
    for pos, valores in enumerate(num):
        print(valores, end=' ')
        sleep(0.3)
        if valores % 2 == 0:
            soma += valores
    sleep(2)
    print()
    print(f'É igual a {soma}')
    print('=' * 50)


numeros = []
sorteia(numeros)
somapar(numeros)