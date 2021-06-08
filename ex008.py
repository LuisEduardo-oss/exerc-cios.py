medida = float(input('qual a medida em metros? '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('decimetros: {}\ncentimetros: {}\nmelimetros: {}\nmetros: {}\ndecametros: {}\nhectometros: {}\nkilometros: {}'.format(dm, cm, mm,medida, dam, hm, km))