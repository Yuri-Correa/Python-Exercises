filme = {}
locadora = []
dec = float
c = 0
print('='*80)
while True:
    filme['Titulo'] = str(input('Nome do filme: '))
    filme['Ano'] = int(input('Ano de lançamento: '))
    filme['Diretor'] = str(input('Diretor: '))
    dec = str(input('Cadastrar novo filme?[S/N] ').upper())
    locadora.append(filme)
    if dec != 'N' and dec != 'S':
        while dec != 'N' and dec != 'S':
            dec = str(input('Resposta Inválida! Cadastrar novo filme?[S/N]').upper())
    if dec == 'N':
        break
print('='*80)
print(f'{"N°.":<20}{"Nome":<20}{"Ano":<20}{"Diretor":>20}')
print('-'*80)
print(locadora)
"""for c in enumerate(locadora):
    print(c, end=' '*20)
    print(locadora[c]['Titulo'])"""