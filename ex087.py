matriz = [[0, 0, 0], [0, 0, 0], [ 0, 0, 0]]
par = 0
col = 0
ma = 0
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            col += matriz[l][2]
        if l == 1:
            if matriz[1][c] > ma:
                ma = matriz[1][c]
print('='*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^8}]', end='')
    print()
print('='*50)
print(f'A soma dos valores pares é igual a: {par}')
print(f'A soma dos valores da terceira coluna é igual a: {col}')
print(f'O maior valor da segunda linha é igual a: {ma}')