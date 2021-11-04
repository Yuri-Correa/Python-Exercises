def dados(nom='<Unknow>', gol=0):
    print(f'O jogador {nom}, marcou {gol} gol(s) no campeonato!')


n = str(input('Nome do jogador: ')).title()
g = str(input('Números de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    dados(gol=g)
else:
    dados(nom=n, gol=g)