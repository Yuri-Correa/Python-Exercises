time = []
aproveitamento = {}
gols = []
while True:
    aproveitamento.clear()
    aproveitamento['Nome'] = str(input('Nome do Jogador: ').title())
    p = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))
    gols.clear()
    for c in range(0, p):
        gols.append(int(input(f'    Quantos gols na {c + 1}° partida ? ')))
    aproveitamento['Gols'] = gols[:]
    aproveitamento['Total'] = sum(gols)
    aproveitamento['Média de Gols'] = float((sum(gols)/p))
    time.append(aproveitamento.copy())
    print('=' * 100)
    while True:
        dec = str(input('Cadastrar novo jogador?[S/N] ').upper()[0])
        if dec in 'SN':
            break
        print('Resposta Inválida!\nDigite apenas S ou N')
    if dec == 'N':
        print('='*100)
        break
    print('=' * 100)
print()
print('-'*100)
print('COD ', end=' ')
for i in aproveitamento.keys():
    print(f'{i:<14}', end='')
print()
print('-'*100)
for k, v in enumerate(time):
    print(f'{k:>2} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*100)
print()
print('='*100)
while True:
    busca = int(input('Mostrar dados de qual jogador?\n(999 para interromper) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Jogador de código {busca} inexistente!')
    else:
        print(f' == LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols')
        print(f'    A média foi de {time[busca]["Média de Gols"]:.2f} gols por partida')
print('FIM')