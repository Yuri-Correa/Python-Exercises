import random
x = str(input('Digite o nome completo: '))
f = x.split()
y = x.upper()
n = y.lower()
t = n.title()
s = t.strip()
l = t.capitalize()
#para colocar em ordem usar sorted()
i = str(input('Palavra para busca: '))
g = str(i in f)
g = g.replace('True', 'Sim')
print(len(x))
print('O primeiro nome é {} e tem {} letras!'.format(f[0], len(f[0])))
print('O total de letras no nome é de {}!'.format(len(x.replace(' ', ''))))
print('{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(x, f, y, n, t, s, l))
print('{}, na posição {}'.format(g, x.find(i)))
print(f)
print(s)