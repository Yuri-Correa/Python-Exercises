m = 0
s = 0
for c in range (0, 5):
    p = float(input('Informe o peso (Kg): '))
    if p > s:
        s = p
        if m == 0:
            m = p
    elif p < m:
        m = p
print('O maior peso informado é {:.2f}Kg e o menor é {:.2f}Kg'.format(s, m))