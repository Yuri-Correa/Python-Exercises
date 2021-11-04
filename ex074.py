from random import randint
a = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números sorteados foram', a[0:6])
b = sorted(a)
print(f'O maior é o', b[4])
print(f'O menor foi', b[0])