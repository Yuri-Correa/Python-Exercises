p = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão de sua PA: '))
s = p
for c in range(0, 10):
    if c == 0:
        print(s, end=' ')
    else:
        s += r
        print(s, end=' ')