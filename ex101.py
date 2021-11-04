from datetime import date


def voto(i):
    idade = date.today().year - i
    if 16 <= idade < 18 or idade >= 65:
        return str(f'Com {idade} anos: VOTO OPCIONAL')
    elif 18 <= idade < 65:
        return str(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade < 16:
        return str(f'Com {idade} anos: NÃO VOTA')


i = int(input('Em que ano você nasceu? '))
print(voto(i))