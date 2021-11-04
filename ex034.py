s = float(input('Informe o valor do salário: '))
#print('Os salários até R$ 1250.00 irão obter um aumento de 15%')
#print('Os salários acima desse valor irão obter um aumento de 10%')
if s <=1250:
    print('O valor do salário era de R$ {:.2f}'.format(s))
    print('O valor atualizado é de R$ {:.2f}'.format(s*1.15))
else:
    print('O valor do salário era de R$ {:.2f}'.format(s))
    print('O valor atualizado é de R$ {:.2f}'.format(s* 1.1))