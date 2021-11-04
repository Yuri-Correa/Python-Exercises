print('-'*23)
print('Sequência de Fibonacci')
print('-'*23)
n = int(input('Termos: '))
if n > 2:
    c = 3
    t1 = 0
    t2 = 1
    print('{} → {}'.format(t1, t2), end='')
    while c <= n:
        t3 = t1 + t2
        print(' → {}'.format(t3), end='')
        c += 1
        t1 = t2
        t2 = t3
elif n == 1:
    print('0')
elif n == 2:
    print('0 → 1')
print('\nFIM')