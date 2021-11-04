from datetime import date
n = int(input('Ano de nascimento:\n'))
a = date.today().year
if a-n>18:
    if (a-n)-18 > 1:
        print('\033[32mJá faz {} anos desde seu alistamento militar!\nSeu alistamento foi no ano de {}'.format((a-n)-18, n+18))
    else:
        print('\033[32mJá faz {} ano desde seu alistamento militar!\nSeu alistamento foi no ano de {}'.format((a-n)-18, n+18))
elif a-n<18:
    if 18-(a-n) > 1:
        print('Ainda falta {} anos para o seu alistamento militar!\nVocê deve se alistar em {}'.format(18-(a-n), n+18))
    else:
        print('Ainda falta {} ano para o seu alistamento militar!\nVocê deve se alistar em {}'.format(18-(a-n), n+18))
elif a-n==18:
    print('\033[31mEsse é o ano do seu alistamento militar!')