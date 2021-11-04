valores = []
c = 0
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    c += 1
    r = str(input('Quer continuar?[S/N] ').upper())
    while r != 'S' and r != 'N':
            r = str(input('Resposta inválida! \nQuer continuar?[S/N] ').upper())
    if r == 'N':
        break
print('='*100)
if c <= 1:
    print(f'O valor digitado foi: {valores}')
else:
    print(f'Você digitou {c} números')
    valores.sort(reverse=True)
    print(f'Os números digitados em ordem descrescente são: {valores}')
if 5 in valores:
    for n, v in enumerate(valores):
        if v == 5:
            print(f'O número 5 está na posição {n+1}!')
else:
    print('O número 5 não faz parte da lista!')
print('Fim')