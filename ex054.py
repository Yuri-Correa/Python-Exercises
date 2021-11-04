from datetime import date
i = date.today().year
s = 0
for c in range (0, 7):
    a = int(input('Ano de nascimento: '))
    d = i - a
    if d >= 18:
        s += 1
print('Dos anos de nascimentos informados {} pessoas são maiores de idade e {} ainda não atingiram a maioridade'.format(s, 7-s))