while True:
    cont = 0
    print('Para sair digite um número negativo!')
    num = int(input('Digite o número para ver sua tabuada: '))
    if num < 0:
        break
    mult = int(input('Digite quantos números deseja na sua tabuada: '))
    if mult < 0:
        break
    print('\n')
    print('-'*30)
    while cont <= mult - 1:
        if mult == 0:
            mult = int(input('Quantidade de Multiplicação não definida!\nDigite quantos números deseja na sua tabuada: '))
        cont += 1
        print(f'{num} X {cont} = {num*cont}')
    print('-'*30)
    print('\n')
print('PROGRAMA TABUADA ENCERRADO! OBRIGADO!')
