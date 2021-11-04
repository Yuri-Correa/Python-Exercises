clas = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico PR', 'São Paulo', 'Internacional',
        'Corinthians', 'Fortaleza EC', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético MG', 'Fluminense',
        'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',	'Chapecoense',	'Avaí')
print('='*100)
ser = str(input('Qual seu time? ').title())
print('='*100)
print('Os cinco primeiros são', clas[0:5])
print('='*100)
print('Os cinco ultimos são', clas[-5:])
print('='*100)
print('Times em ordem alfabética ', sorted(clas))
print('='*100)
print('O seu time é o {} está na {}ª posição'.format(ser, (clas.index(ser))+1))