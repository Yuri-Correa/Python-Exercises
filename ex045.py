from random import randint
from time import sleep
print('Vamos jogar jokenpô!!!')
print('''\nAqui vai as regras:\n1 - Pedra ganha de tesoura mas perde para o papel
2 - Tesoura ganha de papel mas perde para pedra\n3 - Papel ganha de pedra mas perde para a tesoura''')
print('VAMOS LÁ!!')
print('-*-'*60)
j = 0
m = 0
em = 0
r = 1
while r != '':
    e = int(input('Escolha:\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura\n'))
    if e == 1:
        print('\nCerto, você escolheu: 1 - Pedra\n')
    elif e == 2:
        print('\nCerto, você escolheu: 2 - Papel\n')
    elif e == 3:
        print('\nCerto, você escolheu: 3 - Tesoura\n')
    c = randint(1, 3)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!!!!\n')
    sleep(1)
    if e == 1 and c == 3 or e == 2 and c == 1 or e == 3 and c == 2:
        j += 1
        if e == 1:
            print('Você escolheu 1 - Pedra\nE eu escolhi 3 - Tesoura\n\033[1;32mVOCê ME VENCEU!!\n\n\033[m')
        elif e == 2:
            print('Você escolheu 2 - Papel\nE eu escolhi 1 - Pedra\n\033[1;32mVOCê ME VENCEU!!\n\n\033[m')
        elif e == 3:
            print('Você escolheu 3 - Tesoura\nE eu escolhi 2 - Papel\n\033[1;32mVOCê ME VENCEU!!\n\n\033[m')
    elif e == 1 and c == 2 or e == 2 and c == 3 or e == 3 and c== 1:
        m += 1
        if e == 1:
            print('Você escolheu 1 - Pedra\nE eu escolhi 2 - Papel\n\033[1;31mEU VENCI!!\n\n\033[m')
        elif e == 2:
            print('Você escolheu 2 - Papel\nE eu escolhi 3 - Tesoura \n\033[1;31mEU VENCI!!\n\n\033[m')
        elif e == 3:
            print('Você escolheu 3 - Tesoura\nE eu escolhi 1 - Pedra\n\033[1;31mEU VENCI!!\n\n\033[m')
    elif e == c:
        em += 1
        if e == 1:
            print('Você escolheu 1 - Pedra\nE eu escolhi 1 - Pedra\n\033[1;33mEMPATAMOS!\n\n\033[m')
        elif e == 2:
            print('Você escolheu 2 - Papel\nE eu escolhi 2 - Papel\n\033[1;33mEMPATAMOS!\n\n\033[m')
        elif e == 3:
            print('Você escolheu 3 - Tesoura\nE eu escolhi 3 - Tesoura\n\033[1;33mEMPATAMOS!\n\n\033[m')
        sleep(3)
    if j > m:
        print('O placar está {}X{} pra você'.format(j, m))
    elif m > j:
        print('O placar está {}X{} pra mim'.format(m, j))
    elif m == j:
        print('Estamos empatados em {}X{}! Já empatamos {}X!'.format(j, m, em))
    r = input('Digite enter para parar de jogar\nSe quiser jogar novamente aperte qualquer tecla!\n')
if j > m:
    print('O placar Final foi de {}X{} pra você! Parabéns, você venceu o jogo!!!'.format(j, m))
elif m > j:
    print('O placar Final foi de {}X{} pra você! Eu venci o jogo!!!'.format(m, j))
elif m == j:
    print('Empatamos em {}X{}! Teve {} partidas empatadas!'.format(j, m, em))