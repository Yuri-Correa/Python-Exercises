r = float(input('Quantos reais você tem?\n'))
d = float(input('Qual a cotação atual do Dólar?\n'))
print('Com a cotação atual do dólar em {} você pode converter seus {} reais em {:.2f} dólares'.format(d, r, r/d))