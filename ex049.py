x = int(input('Digite um número: '))
n = 0
m = int(input('Digite até qual multiplicador irá sua tabuada: '))
for c in range(0, m+1):
    print('A tabuada do número {} é:\n{}x{} = {}'.format(x, x, n, x*n))
    n += 1