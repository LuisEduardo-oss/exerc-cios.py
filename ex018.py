import math
an = int(input('qual angulo deseja calcular? '))
seno = math.sin(math.radians(an))
print('o angulo de {} tem o SENO de {:.2f}'.format(an, seno))
coss = math.cos(math.radians(an))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(an, coss))
tan = math.tan(math.radians(an))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))