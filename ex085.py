num = []
par = []
imp = []
for c in range(0, 7):
    temp = int(input(f'Digite o {c+1}º número: '))
    if temp % 2 == 0:
        par.append(temp)
        par.sort()
    else:
        imp.append(temp)
        imp.sort()
num.append(par[:])
num.append(imp[:])
print('='*50)
print(f'Os números pares digitados foram: {num[0]}')
print(f'Os números ímpares digitados foram: {num[1]}')
