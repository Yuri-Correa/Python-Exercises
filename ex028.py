from random import randint
n = int(randint(0, 5))
print('Pensei em um número!')
a = int(input('Advinhe em qual número, de 0 a 5, eu pensei!\n'))
if n == a:
    print('PARABÉNS VOCê ACERTOU!')
else:
    if a > 5:
        print('Tem que ser um número até 5!')
    else:
        print('Puxa, você errou. O número era {}'.format(n))
