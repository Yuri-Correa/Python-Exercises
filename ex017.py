from math import sqrt
b = float(input('Insira o primeiro cateto:\n'))
c = float(input('Insira o segundo cateto:\n'))
a = sqrt(b**2+c**2)
print('O valor da hipotenusa é:\n{}'.format(a))