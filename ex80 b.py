lista = []
print('='*60)
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        if c == 0:
            print('O valor foi adicionado a lista')
        else:
            print('O valor foi adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'O valor foi adicionado a posição {pos}')
                break
            pos += 1
print('='*60)
print(f'Os valores digitados foram {lista}')