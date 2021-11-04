from datetime import date
nome = str(input('Insira o nome do atleta:\n'))
i = int(input('Insira o ano de nascimento do atleta:\n'))
a = date.today().year
c = a-i
if c<=9:
    print('A categoria do atleta {} é MIRIM'.format(nome))
elif 9<c<=14:
    print('A categoria do atleta {} é INFANTIL'.format(nome))
elif 14<c<=19:
    print('A categoria do atleta {} é JUNIOR'.format(nome))
elif c==20:
    print('A categoria do atleta {} é SÊNIOR'.format(nome))
elif c>20:
    print('A categoria do atleta {} é MASTER'.format(nome))