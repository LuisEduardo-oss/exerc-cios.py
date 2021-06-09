print('_='*20)
print('analisador de triangulos')
print('_='*20)
r1 = float(input('qual o valor do primeiro segmento? '))
r2 = float(input('qual o valor do segundo segmento? '))
r3 = float(input('qual o valor do terceiro segmento? '))
if r1 < r2 + r3 and r2 < r1 +  r3 and r3 < r2 + r1:
    print('os segmentos acima PODEM SE TORNAR UM TRIANGULO')
else:
    print('os segmentos acima NÃO PODEM SE TORNAR UM TRIANGULO')