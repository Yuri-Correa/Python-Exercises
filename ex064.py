numero = 0
cont = 0
soma = 0
print('-'*35)
print('Para parar digite o número 999')
print('-'*35)
while numero != 999:
    numero = int(input('Digite o número: '))
    if numero != 999:
        soma += numero
        cont += 1
if cont == 1:
    print('\nVocê digitou {} número!\nO valor do número é de {}!\n'.format(cont, soma))
else:
    print('\nVocê digitou {} números!\nA soma dos números é {}!\n'.format(cont, soma))
print('\nFIM\n')