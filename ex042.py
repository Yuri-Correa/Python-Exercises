a = float(input('Informe o comprimento da primeira reta: '))
b = float(input('Informe o comprimento da segunda reta: '))
c = float(input('Informe o comprimento da terceira reta: '))
if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        print('Essas retas formam um triângulo Equilatero!')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('Essas retas formam um triângulo Isósceles!')
    elif a != b and a != c and b != c:
        print('Essas retas formam um triângulo Escaleno!')
else:
    print('Não é possível formar um triângulo!')
