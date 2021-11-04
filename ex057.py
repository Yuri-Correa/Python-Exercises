n = str(input('Nome: '))
s = str('a')
s = str(input('Sexo [M/F]: ')).upper()
while s not in 'MF':
    s = str(input('Dados inválidos. Por favor nos informe seu Sexo [M/F]: ')).upper()
if s == 'F':
    print('Bom dia senhorita {}'.format(n.capitalize()))
else:
    print('Bom dia senhor {}'.format(n.capitalize()))