n = str(input('Digite seu nome completo: '))
t = 'SILVA' in n.upper()
if t == True:
    print('Seu nome possui Silva')
else:
    print('Seu nome não possui Silva')

#print('Seu nome possui Silva: {}'.format('SILVA' in n.upper()))
