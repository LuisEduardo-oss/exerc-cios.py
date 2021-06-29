n1 = int(input('primeiro segmento: '))
n2 = int(input('segundo segmento: '))
n3 = int(input('terceiro segmento: '))
if n1 == n2 and n2 == n3 and n3 == n1:
    print('triangulo: EQUILÁTERO')
elif n1 == n2 or n2 == n3 or n3 == n1:
    print('triangulo: ISÓCELES')
else:
    print('triangulo: ESCALENO')