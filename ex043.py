p = float(input('Peso: '))
a = float(input('Altura: '))
imc = p/a**2
if imc < 18.5:
    print('Seu IMC é: {:.2f}\nVocê esta abaixo do peso!'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é: {:.2f}\nVocê esta com o peso ideal!'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é: {:.2f}\nVocê esta com sobrepeso!'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é: {:.2f}\nVocê esta obeso!'.format(imc))
elif imc > 40:
    print('Seu IMC é: {:.2f}\nVocê esta com obesidade mórbida!'.format(imc))