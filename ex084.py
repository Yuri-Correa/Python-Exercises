cadastros = []
dados = []
ma = me = 0
while True:
    dados.append(str(input('Nome: ').title()))
    dados.append(float(input('Peso: ')))
    if len(cadastros) == 0:
        ma = me = dados[1]
    else:
        if dados[1] > ma:
            ma = dados[1]
        elif dados[1] < me:
            me = dados[1]
    cadastros.append(dados[:])
    dados.clear()
    r = str(input('Novo Cadastro?[S/N] '))
    if r in 'Nn':
        break
    else:
        while r != 'S' and r != 's':
            r = str(input('Resposta Inválida!\nFazer novo cadastro?[S/N] '))
print(f'Cadastros: {len(cadastros)}')
print(f'O maior peso foi de {ma}Kg do(a): ', end='')
for c in cadastros:
    if c[1] == ma:
        print(c[0], end='')
print(f'\nO menor peso foi de {me}Kg do(a): ', end='')
for c in cadastros:
    if c[1] == me:
        print(c[0], end='')
print('Fim')