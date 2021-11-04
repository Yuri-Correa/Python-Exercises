from math import sin, cos, tan, radians
ang = int(input('Informe o ângulo\n'))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Seno: {:.2f}\nCosseno:{:.2f}\nTangente:{:.2f}'.format(sin, cos, tan))
