a = float(input('Informe o comprimento da primeira reta: '))
b = float(input('Informe o comprimento da segunda reta: '))
c = float(input('Informe o comprimento da terceira reta: '))
if a+b>=c and a+c>=b and c+b>=a:
    print('Essas retas podem formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')