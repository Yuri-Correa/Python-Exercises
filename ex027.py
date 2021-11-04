n = str(input('Digite seu nome completo:\n'))
n = n.split()
i = len(n)
print('Primeiro nome: {}\nUltimo Nome: {}'.format(n[0], n[i-1]))
