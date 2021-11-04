'''num = [2, 3, 6, 5, 9]
#num[2] = int(input(''))
#a = int(input('x'))
#num.append(a)
print(num)
num.sort(reverse=True)
num.insert(2, 235)
print(len(num))
#print(num[5])
print(num)
num.pop(3)
print(num)
del num[1]
print(num)
if 2 in num:
    num.remove(235)
print(num)'''
from random import randint
valores = list()
num = valores
valores.append(randint(0, 100))
valores.append(randint(0,10))
valores.append(randint(0,1000))
print(valores)
for c, v in enumerate(valores):
    print(f'O valor {v} está na posição {c}')
valores.sort()
print(valores)
for c in range(0, 3):
    valores.append(int(input('Digite um valor: ')))
valores.sort()
print(valores)
num.sort(reverse=True)
print(num)