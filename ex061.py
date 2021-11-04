p = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão de sua PA: '))
c = 0
while c <= 9:
    if c == 0:
        print(p, end=' ')
    else:
        p += r
        print(p, end=' ')
    c += 1