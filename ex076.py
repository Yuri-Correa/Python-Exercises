lista = ('Computador', 27000, 'Mouse', 350, 'Caderno', 25, 'HD Externo', 400,\
         'Livro', 25, 'Estojo', 10, 'Fone', 10, 'HD SSD', 500)
print('='*52)
print('Preços'.center(52))
print('='*52)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<40}', end='')
    else:
        print(f'R$ {lista[item]:>8.2f}')
print('='*52)