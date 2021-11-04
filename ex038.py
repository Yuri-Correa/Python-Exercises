n = int(input('Insira o primeiro número: '))
m = int(input('Insira o segundo número: '))
if n>m:
    print('O número {} é maior que o número {}!'.format(n, m))
elif m>n:
    print('O número {} é maior que o número {}!'.format(m, n))
else:
    print('Não existe valor maior, os dois valores {} e {} são iguais!'.format(n, m))