peso = float(input('digite seu peso: '))
altura = float(input('digite sua alura: '))
imc = peso / (altura ** 2)
print('seu IMC foi:{:.1f}'.format(imc))
if imc <=18.5:
    print('ABAIXO do peso')
elif 18.5 <= imc >25:
    print('peso IDEAL')
elif 25 >= imc < 30:
    print('SOBREPESO')
elif 30 >= imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBSIDADE MÓRBITA')

