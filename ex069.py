m = 0
h = 0
ha = 0
mc = 0
ma = 0
hc = 0
cont = 0
print('Cadastro de pessoa')
print('-'*40)
while True:
    idade = int(input('Digite a Idade da pessoa: '))
    sex = str(input('Digite o sexo da pessoa[M/F]: ').upper())
    while sex not in 'FM':
        sex = str(input('Digite o sexo da pessoa[M/F]: ').upper())
    if sex == 'M' or sex == 'F':
        if sex == 'F':
            m += 1
            if idade >= 18:
                ma += 1
            else:
                mc += 1
        elif sex == 'M':
            h += 1
            if idade >= 18:
                ha += 1
            else:
                hc += 1
    print('-'*40)
    decis = str(input('Cadastrar nova pessoa? [S/N] ').upper())
    while decis not in 'SN':
            decis = str(input('Cadastrar nova pessoa? [S/N] ').upper())
    print('-'*40)
    if decis == 'N':
        break
    cont += 1
print('-'*40)
print(f'Você cadastrou: \n{ma+ha} maiores de 18 anos;')
print(f'{h} Homens;')
print(f'{m} Mulheres;')
print(f'{ma} Mulheres maiores de 18;')
print(f'{ha} Homens maiores de 18;')
print(f'{mc} Mulheres menores de 18;')
print(f'{hc} Homens menores de 18;')
print(f'Total de pessoas cadastardas: {cont}')
print('-'*40)