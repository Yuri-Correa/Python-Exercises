from datetime import date
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
Nascimento = int(input('Ano de Nascimento: '))
cadastro['CTPS'] = int(input('Nr° CTPS (0 não tem): '))
cadastro['Idade'] = date.today().year - Nascimento
if cadastro['CTPS'] != 0:
    Contratação = int(input('Ano da primeira contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = (Contratação - Nascimento) + 35
print()
print('='*50)
print()
for k, v in cadastro.items():
    print(f'{k}: {v}')