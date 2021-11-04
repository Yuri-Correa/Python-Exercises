r = int(input('Até qual número você quer somar? '))
m = int(input('Multiplos de qual número? '))
c = int(input(
    'Digite:\n[ 1 ] - Para somar todos os números\n[ 2 ] - Para somar somente os pares\n[ 3 ] - Para somar somente os ímpares\n'))
s = 0
n = 0
if c == 1:
    for c in range(1, r + 1):
        if c % m == 0:
            s += c
            n += 1
elif c == 2:
    for c in range(0, r+1, 2):
        if c % m == 0:
            s += c
            n += 1
elif c == 3:
    for c in range(1, r + 1, 2):
        if c % m == 0:
            s += c
            n += 1
else:
    print('Opção Inválida')
print('A soma dos {} números é: {}'.format(n, s))
