n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
if m<5:
    print('\033[31mSua média foi {:.2f}!\nREPROVADO! SINTO MUITO!\033[m'.format(m))
elif 5==m or m<6.9:
    print('\033[33mSua média foi {:.2f}!\nRECUPERAÇÃO! PRECISA ESTUDAR MAIS!\033[m'.format(m))
elif m>7:
    print('\033[32mSua média foi {:.2f}!\nPARABÉNS! VOCÊ FOI APROVADO!'.format(m))