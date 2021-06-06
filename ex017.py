#cataj = float(input('qual o valor do cateto adjacente?  '))
#catop = float(input('qual o valor do cateto oposto? '))
#hip = (catop ** 2 + cataj ** 2) ** (1/2)
#print('a medida da hipotenusa vale: {}'.format(hip))
from math import hypot
co = float(input('valor do cateto oposto: '))
ca = float(input('valor do cateto adjacente: '))
hi = hypot(co, ca )
print('o valor da hipotenusa é: {:.2f}'.format(hi))
