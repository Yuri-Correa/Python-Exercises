c = 0
t = int(input('Digite quantos termos: '))
a = 0
f = 0
te = 0
if t != 0:
    p = int(input('Digite o primeiro termo da sua PA: '))
    while t != 0:
        if t != 1:
            if t > 1:
                r = int(input('Digite a razão de sua PA: '))
            while t != 0:
                if t > 1:
                    f = p
                    print('\nPA: ', end='')
                    while c <= t-1:
                        if c == 0:
                            print(f, end=' ')
                        elif 0 < c:
                            f += r
                            print(f, end=' ')
                            if c == t-1:
                                c += 1
                        c += 1
                    if c > t:
                        te = t
                        print('\nProgreção aritmética com {} termos'.format(te))
                        print('\n\nPara sair digite 0 na quantidade de Termos')
                        a = int(input('\nQual a quantidade de termos você deseja adicionar a sua progreção?\n'))
                        if a != 0:
                            t = t + a
                            c = 0
                        else:
                            te = t
                            t = 0
        else:
            print('\nPA: ', end='')
            print(p, end=' ')
            print('\nProgreção aritmética com {} termo'.format(1))
            print('\n\nPara sair digite 0 na quantidade de Termos')
            a = int(input('\nQual a quantidade de termos você deseja adicionar a sua progreção?\n'))
            if a != 0:
                t = t + a
            else:
                t = 0
print('Quantidade de termos na sua progreção aritmética final: {}'.format(te))
print('fim')