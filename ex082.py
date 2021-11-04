lista = []
listapar = []
listaimpar = []
i = p = 0
print('='*60)
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Adicionar outro valor?[S/N] ').upper())
    if r in 'SsNn':
        if r in 'Nn':
            break
    else:
        while r != 'S' and r != 'N':
            r = str(input('Resposta Inválida!\nAdicionar outro valor?[S/N] ').upper())
        if r == 'N':
            break
for c in range(len(lista)):
    if lista[c] % 2 == 0:
        listapar.append(lista[c])
        p += 1
    else:
        listaimpar.append(lista[c])
        i += 1
print('='*60)
print(f'Os números que você digitou são: {lista}')
if p != 0:
    listapar.sort()
    print(f'Você digitou os numeros pares: {listapar}')
else:
    print('Você não digitou valores pares!')
if i != 0:
    listaimpar.sort(reverse=True)
    print(f'Você digitou os numeros impares: {listaimpar}')
else:
    print('Você não digitou valores impares!')
print('='*60)
print('Fim')