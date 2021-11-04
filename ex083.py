ex = str(input('Digite sua expressão: '))
ex.split()
p = 0
for c in range(len(ex)):
    if ex[c] in '()':
       p += 1
if p % 2 == 0:
    print('A expressão é válida!')
else:
    print('Sua expressão está errada!')