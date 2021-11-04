from random import randint
from time import sleep
print('='*51)
print(' '*20, 'MEGA SENA')
print('='*51)
jogo = []
num = []
q = int(input('Quantos jogos deseja fazer? '))
print('='*16, f'Sortenado {q} Jogos', '='*16, '\n')
for c in range(0, q):
    for n in range(0, 6):
        n = randint(1, 60)
        while n in num:
            n = randint(1, 60)
        num.append(n)
    num.sort()
    jogo.append(num[:])
    num.clear()
for j in range(0, q):
    print(f'Jogo {j+1}: {jogo[j]}')
    sleep(1)
print()
print('='*20, 'Boa Sorte', '='*20)
print('Fim')