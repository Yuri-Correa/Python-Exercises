from random import randint
c = 0
n = int(randint(0, 10))
print('Pensei em um número!')
a = int(input('Advinhe em qual número, de 0 a 10, eu pensei!\n'))
while n != a:
    if a > 10:
        print('Tem que ser um número até 10!')
    else:
        print('Puxa, você errou. Tente novamente!')
    a = int(input('Digite o número: '))
    c += 1
print('PARABÉNS VOCÊ ACERTOU! Você usou {} chances!!!'.format(c))

