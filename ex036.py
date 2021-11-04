v = float(input('Valor da casa\nR$ '))
m = 12*float(input('Em quantos anos:\n'))
s = float(input('Salário do comprador:\nR$ '))
p = v/m
if p>s*0.3:
    print('\033[1:31mValor da casa R$ {:.2f}\nPara ser pago em {:.0f} meses\nEm parcelas de R$ {:.2f}\033[m'.format(v, m, p))
    print('\033[1:31mO empréstimo não pode ser concedido.\nPois a parcela excedeu o limite de 30% do salário\033[m')
else:
    print('\033[1:32mValor da casa R$ {:.2f}\nPara ser pago em {:.0f} meses\nEm parcelas de R$ {:.2f}\033[m'.format(v, m, p))
    print('\033[1:32mO empréstimo pode ser concedido.\nPois a parcela esta dentro do limite de 30% do salário\033[m')