print('Boletim:')
boletim = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = ((n1+n2)/2)
    boletim.append([nome, [n1, n2], med])
    r = (str(input('Deseja continuar? [S/N] ').upper()))
    if r in 'Nn':
            break
    else:
        while r != 'S' and r != 's' and r != 'N' and r != 'n':
            r = str(input('Resposta Inválida! Deseja continuar?[S/N] '))
        if r in 'Nn':
            break
    print('='*63)
    print(f'{"N°.":<21}{"Nome":<21}{"Média":>21}')
    print('-'*63)
    for c, i in enumerate(boletim):
        print(f'{c:<21}{i[0]:<21}{i[2]:>21.2}')
    while True:
        print('='*63)
        ind = int(input('Qual aluno deseja visualizar as notas (999 para interromper):\n'))
        if ind == 999:
            break
        if ind <= len(boletim) -1:
            print(f'Notas de {boletim[ind][0]} são {boletim[ind][1]}')
    print('Fim...')