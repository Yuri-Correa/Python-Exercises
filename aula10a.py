t = int(input('Em qual ano foi fabricado seu carro?\n'))
c = int(input('Em que ano estamos?\n'))
c = c-t
if c <= 2:
    print('Seu carro esta novo!')
else:
    print('Seu carro esta velho, melhor fazer revisões periodicamente!')