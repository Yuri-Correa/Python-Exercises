def leiaint(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Valor inserido não é um número inteiro!')
        if ok:
            break
    return valor


numero = leiaint('Digite um número: ')
print(f'O valor digitado foi {numero}')
