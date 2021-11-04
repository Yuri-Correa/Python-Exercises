m = 0
iv = 0
l = 0
for c in range (0, 4):
    print('----- {}ª Pessoa -----'.format(c+1))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    g = str(input('Gênero [M/F]: ')).upper()
    m += i
    if g == 'M':
        if i > iv:
            mv = n
            iv = i
    elif g == 'F':
        if i < 20:
          l += 1
print('A idade média do grupo é {}'.format(m/4))
if iv != 0:
    print('O homem mais velho é o {} que possui {} anos'.format(mv, iv))
if l > 1:
    print('{} mulheres possuem menos de 20 anos'.format(l))
elif l == 1:
    print('{} mulher possui menos de 20 anos'.format(l))