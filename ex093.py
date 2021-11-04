aproveitamento = {}
gols = []
aproveitamento['Nome'] = str(input('Nome do Jogador: ').title())
p = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))
for c in range(0, p):
    gols.append(int(input(f'    Quantos gols na {c + 1}° partida ? ')))
aproveitamento['Gols'] = gols[:]
aproveitamento['Saldo de Gols'] = sum(gols)
print('='*100)
print(aproveitamento)
print('='*100)
for k, v in aproveitamento.items():
    print(f'{k}: {v}')
print('='*100)
print(f'O jogador {aproveitamento["Nome"]} jogou {len(aproveitamento["Gols"])} partidas: ')
for c in range(0, p):
    print(f'=> Na {c+1}° partida, fez {gols[c]} gols ')
print(f'Foi um total de {aproveitamento["Saldo de Gols"]} gols')