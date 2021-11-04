num = 'zero', 'um', 'dois', 'três', 'quatro', ' cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', \
      'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
ch = int(input('Digite um número inteiro entre 0 e 20: '))
while True:
    if 0 > ch or 20 < ch:
        ch = int(input('Tente de novo. Digite um número inteiro entre 0 e 20: '))
    if 0 <= ch <= 20:
        print(f'Você digitou o número {num[ch]}')
        break
print('Fim')
