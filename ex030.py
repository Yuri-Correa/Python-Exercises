n = int(input('Digite um número: '))
m = n%2
if m == 0:
    print(f'O número {n} é par!')
else:
    print('O número {} é impar!'.format(n))