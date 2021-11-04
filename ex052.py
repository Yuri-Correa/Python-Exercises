p = int(input('Digite um número: '))
s = 0
for c in range(1, p+1):
    if p % c == 0 and p != c and c != 1 and c != 0:
        s += 1
if s >= 1:
    print('O número {} não é um número primo!'.format(p))
else:
    print('O número {} é um número primo!'.format(p))