def notas(*n, sit=False):
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Media'] >= 5:
            r['Situação'] = 'Mediana'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = notas(1, 5, 7, 8, 10, 10, sit=True)
print(resp)