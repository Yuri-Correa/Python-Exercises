def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


num = int(input('Digite um  número inteiro: '))
fat = fatorial(num)
print(f'O fatorial do numero {num} é {fat}')
