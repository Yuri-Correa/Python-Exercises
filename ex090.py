boletim = {}
dec = str
boletim['Nome'] = str(input('Nome do aluno: ').title())
boletim['Média'] = float(input(f'Media {boletim["Nome"]}: '))
if boletim['Média'] < 5:
    boletim['Situação'] = str('Aluno reprovado')
elif 5 <= boletim['Média'] < 7:
    boletim['Situação'] = str('Aluno de recuperação! Precisa melhorar!')
else:
    boletim['Situação'] = str('Aluno aprovado! Parabens!')
for k, v in boletim.items():
    print(f'{k}: {v}')