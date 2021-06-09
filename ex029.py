km = int(input('quantos km/h voce estava? '))
multa = (80 - km) * 7
if km > 80:
    print('você sera multado por estar en alta velocidade')
    print('o valor da multa é: {}'.format(multa))
else:
    print('você esta na velocidade adquada, não sera multado')