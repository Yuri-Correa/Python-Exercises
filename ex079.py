num = list()
add = 0
print('='*50)
while True:
    add = int(input('Digite um valor: '))
    if add in num:
        print('Número Duplicado! Não irei adicionar na lista...')
    else:
        num.append(add)
        print('Número Adicionado com sucesso...')
    r = str(input('Adicionar outro Valor? [S/N] ').upper())
    if r != 'S' and r != 'N':
        while r != 'S' and r != 'N':
            r = str(input('Resposta Inválida!\nAdicionar outro Valor? [S/N] ').upper())
    if r == 'N':
        break
print('='*50)
num.sort()
print(f'Você digitou os números: {num}')