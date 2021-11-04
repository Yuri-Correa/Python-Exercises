n = int(input('Informe um numero: '))
m = n//1000
c = (n%1000)//100
d = ((n%1000)%100)//10
u = (((n%1000)%100)%10)//1
print('Milhar: {:^10}\nCentena: {:^8}\nDezena: {:^10}\nUnidade: {:^8}\n'.format(m, c, d, u))
