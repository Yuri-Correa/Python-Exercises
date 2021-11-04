from time import sleep


def maior(* valores):
    cont = maior = 0
    print('='*50)
    print('Analisando os valores...')
    for valor in valores:
        sleep(0.5)
        print(f'{valor}', end=' ')
        cont += 1
        if valor > maior:
            maior = valor
    print(f'\nForam inseridos {cont} valores')
    print(f'O maior valor inserido foi {maior}.')
    print('='*50)
    sleep(3)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()