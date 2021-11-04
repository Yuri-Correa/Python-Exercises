v = float(input('Qual era a velocidade do veículo?\n'))
m = (v-80)*7
if m <= 0:
    print('O veículo estava dentro do limite de velocidade!')
else:
    print('O veiculo estava {:.0f} Km/h acima do limite de 80 Km/h'.format(v-80))
    print('O valor da multa será de R$ {:.2f}'.format(m))