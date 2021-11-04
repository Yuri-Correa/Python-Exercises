c = int(input('Digite um número: '))
f = 1
print('{}!'.format(c), end='=')
while c != 0:
    print('{}'.format(c), end='')
    if c != 0:
        f = f*c
        if c != 1:
            print('x', end='')
    c = c-1
print('={}'.format(f))