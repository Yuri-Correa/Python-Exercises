estado = {}
brasil = []
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: ').title())
    estado['Sigla'] = str(input('Sigla do estado: ').upper())
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'A {k} é {v}')