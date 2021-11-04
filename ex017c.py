from math import sqrt, pow
b = float(input('Informe o cateto adjacente:\n'))
c = float(input('Informe o cateto oposto:\n'))
a = sqrt((pow(b, 2)+pow(c, 2)))
print('A Hipotenusa é de:\n{}'.format(a))