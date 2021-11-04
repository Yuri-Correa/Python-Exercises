cont = 0
contp = 0
som = 0
pb = 0
while True:
    nome = str(input('Nome do produto: ').title())
    preço = float(input('Preço: '))
    if preço > 1000:
        contp += 1
    if cont == 0 or preço < pb:
        pb = preço
        bn = nome
    som += preço
    cont += 1
    decis = str(input('Continuar?[S/N] ').upper())
    while decis not in 'SN':
        decis = str(input('Continuar?[S/N] ').upper())
    if decis == 'N':
        break
    print('')
print('-'*40)
print(f'Itens comprados: {cont}')
print(f'Itens com valor superior a R$ 1000,00: {contp}')
print(f'Item mais barato: {bn}\nValor do item: R${pb:.2f}')
print(f'Valor total da compra: R${som:.2f}')
print('-'*40)