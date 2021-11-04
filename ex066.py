cont = 0
soma = 0
print('-'*40)
print('Para finalizar o programa digite 999!')
print('-'*40,'\n')
while True:
    número = int(input('Digite um valor: '))
    cont += 1
    if número == 999:
        break
    soma += número
if cont > 1:
    print(f'\nVocê digitou {cont} números')
    print(f'A soma dos números digitados é {soma}')
elif cont == 1:
    print(f'Você digitou {cont} número')
    print(f'O npumero que você digitou é {soma}')
