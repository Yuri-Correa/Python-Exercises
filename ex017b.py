from math import hypot
b = float(input('Insira o primeiro cateto:\n'))
c = float(input('Insira o segundo cateto:\n'))
a = hypot(b, c)
print('O valor da hipotenusa é:\n{}'.format(a))
