a = ('Gustavo', 'Nicoly', 'Elaine', 'Egmar', 'Junior', 'Dantas', 'Rafael', \
     'Seiky', 'Laryssa', 'Bella', 'Aurora', 'Yuri')
for c in a:
    print(f'\nA palavra {c.upper()} tem as vogais: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')