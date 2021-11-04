preço = float(input('Preço do produto R$: '))
print('Condiçoes de pagamento:')
condi = int(input(' 1 - À Vista em dinheiro/cheque\n 2 - À Vista no cartão\n 3 - Parcelado em até 2x no cartão\n 4 - Parcelado no cartão\n\n'))
if condi == 1:
    pagamento = preço-(preço*0.1)
    print('\nValor produto R$ {}'.format(preço))
    print('Valor Final\nR$: {:.2f}'.format(pagamento))
elif condi == 2:
    pagamento = preço - (preço * 0.05)
    print('\nValor produto R$ {}'.format(preço))
    print('Valor Final\nR$: {:.2f}'.format(pagamento))
elif condi == 3:
    parcelas = 2
    pagamento = preço/parcelas
    print('\nValor produto R$ {}'.format(preço))
    print('Valor dividido em {}X de\nR$: {:.2f}'.format(parcelas, pagamento))
elif condi == 4:
    parcelas = int(input('\nEm quantas vezes: '))
    pagamento = (preço*1.2)/parcelas
    print('Valor do produto R$ {}'.format(preço))
    print('Valor dividido em {}X de\nR$: {:.2f}'.format(parcelas, pagamento))
    print('Valor Final com juros\nR$ {:.2f}'.format(preço*1.2))
else:
    print('\033[31mOPÇÃO INVÁLIDA\033[m')