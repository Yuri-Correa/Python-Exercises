d = float(input('Informe qual a distância da viagem: '))
if d <= 200:
    print('O valor da passagem é R$ {:.2f}'.format(d*0.5))
else:
    print('O valor da passagem é R$ {:.2f}'.format(d*0.45))