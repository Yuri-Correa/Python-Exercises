def area(l, c):
    print(f'A área do terreno {l}x{c} é de: {l * c} m²')


def tit(a):
    nomedoprograma = a
    print('='*100)
    print(nomedoprograma.center(100).title())
    print('='*100)


tit('Terreno')
l = float(input('Largura do terreno(m): '))
c = float(input('Comprimento do terreno(m): '))
area(l, c)