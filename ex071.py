print('-'*50)
print('Cédulas disponíveis R$ 50,00  20,00  10,00  1,00')
print('-'*50)
saq = int(input('Valor para saque: '))
while True:
    val = saq
    n5 = 0
    n2 = 0
    n1 = 0
    n = 0
    if saq != 0:
        while saq != 0:
            if saq >= 50:
                saq -= 50
                n5 += 1
            elif 20 <= saq < 50:
                saq -= 20
                n2 += 1
            elif 10 <= saq < 20:
                saq -= 10
                n1 += 1
            else:
                saq -= 1
                n += 1
        print('-'*50)
        if n5 != 0:
            print(f'{n5} notas de R$ 50,00')
        if n2 != 0:
            print(f'{n2} notas de R$ 20,00')
        if n1 != 0:
            print(f'{n1} notas de R$ 10,00')
        if n != 0:
            print(f'{n} notas de R$ 1,00')
        print('-'*50)
        if saq == 0:
            print('Se não deseja realizar novo saque digite o valor = 0')
            saq = int(input('Valor para novo saque: '))
            if saq == 0:
                break
    else:
        break
print('Fim')