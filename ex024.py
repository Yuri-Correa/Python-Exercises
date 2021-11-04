n = str(input('Digite o nome de uma cidade: \n'))
n = n.upper()
n = n.split()
i = 'SANTO' in n[0]
if i:
    print('O nome da cidade começa com Santo!')
else:
    t = 'SÃO' in n[0]
    if t:
        print('O nome da cidade começa com São!')
    else:
        print('O nome da cidade não tem nada referente a Santo no nome!')


