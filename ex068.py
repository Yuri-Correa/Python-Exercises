from random import randint
pw = 0
while True:
    player = 0
    computer = 0
    cw = 0
    choose = str(input('Escolha Par ou Impar: ').upper())
    if choose == 'PAR':
        player = int(input('Digite o Valor: '))
        computer = int(randint(0, 10))
        result = (player+computer)%2
        if result == 0:
            print(f'\nEu escolhi o número {computer}')
            print('Você me venceu!')
            pw += 1
        elif result != 0:
            print(f'\nEu escolhi o número {computer}')
            print('Eu venci!')
            cw += 1
    elif choose == 'IMPAR':
        player = int(input('Digite o Valor: '))
        computer = int(randint(0, 10))
        result = (player+computer)%2
        if result != 0:
            print(f'\nEu escolhi o número {computer}')
            print('Você me venceu!')
            pw += 1
        elif result == 0:
            print(f'\nEu escolhi o número {computer}')
            print('Eu venci!')
            cw += 1
    if cw == 1:
        break
print('Fim de Jogo!!')
if pw > 1:
    print(f'Você me venceu {pw} vezes!')
elif pw == 1:
    print('Você conseguiu me vencer 1 vez!')
elif pw == 0:
    print('Puxa, você está sem sorte, não conseguiu me vencer!')