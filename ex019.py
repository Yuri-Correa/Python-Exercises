from random import choice
a = str(input('Informe o primeiro aluno: '))
b = str(input('Informe o segundo aluno: '))
c = str(input('Informe o terceiro aluno: '))
d = str(input('Informe o quarto aluno: '))
list = [a, b, c, d]
print('O aluno escolhido foi:\n{}'.format(choice(list)))