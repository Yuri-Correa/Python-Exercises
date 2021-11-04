name = input('Insira o nome do Aluno:\n')
note1 = float(input('Primeira nota:\n'))
note2 = float(input('Segunda nota:\n'))
print('\n\nO aluno {} obteve as notas:\n{}\n{}\nSua Média é:\n{}'.format(name, note1, note2, (note1+note2)/2))