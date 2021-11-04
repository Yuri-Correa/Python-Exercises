cadastro = []
pessoas = {}
soma = média = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ').title())
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]: ').upper()[0])
        if pessoas['Sexo'] in 'MF':
            break
        print('Resposta Inválida!\nDigite apenas M ou F')
    pessoas['Idade'] = int(input('Idade: '))
    cadastro.append(pessoas.copy())
    soma += pessoas['Idade']
    print('='*75)
    while True:
        dec = str(input('Deseja fazer um novo cadastro?[S/N] ').upper()[0])
        if dec in 'SN':
            break
        print('Resposta Inválida!\nDigite apenas S ou N')
    if dec == 'N':
        break
    print('='*75)
print('='*75)
print(f'Pessoas {len(cadastro)} cadastradas\n')
média = soma/len(cadastro)
print(f'Média de idedade do grupo: {média:5.2f} anos\n')
print('As mulheres cadastradas foram : ')
for p in cadastro:
    if p['Sexo'] == 'F':
        print('.' * 33, end='')
        print(f'{p["Nome"]}')
print()
print('Pessoas com idade acima da média:')
for p in cadastro:
    if p['Idade'] > média:
        print('.'*35, end='')
        print(f'{p["Nome"]}')