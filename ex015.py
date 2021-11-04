d = int(input('Quantos dias de aluguel?\n'))
km = float(input('Qual a Kilometragem rodada?\n'))
print('O carro alugado por {} dias percorreu {}Km'.format(d, km))
print('O valor do aluguel é de:\nR$ {:.2f}'.format(60*d+km*0.15))