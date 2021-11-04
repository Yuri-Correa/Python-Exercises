from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    elif p < 0:
        p = p * -1
    print('=' * 50)
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    elif i > f:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('='*50)
print('Agora é sua vez! Personalize a contagem: ')
inic = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(inic, fim, pas)
