valores = list()
ma = 0
me = 0
print('='*60)
while True:
    for c in range(0, 5):
        valores.append(int(input(f'Digite o {c+1}º número: ')))
        if c == 0:
            ma = me = valores[c]
        else:
            if valores[c] > ma:
                ma = valores[c]
            elif valores[c] < me:
                me = valores[c]
    print('='*60)
    print(f'Os valores digitados foram: {valores}', end='')
    print()
    print(f'O maior valor digitado foi {ma} na posição: ',end='')
    for p,v in enumerate(valores):
        if v == ma:
            print(f'{p}...')
    print(f'O menor valor digitado foi {me} na posição: ',end='')
    for p,v in enumerate(valores):
        if v == me:
            print(f'{p}...')
    print('=' * 60)
    r = str(input('Tentar de novo? [S/N]').upper())
    if r == 'N':
        break
    else:
        print('='*60)
print('FIM')
