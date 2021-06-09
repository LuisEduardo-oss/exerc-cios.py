a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
print('o menor valor digitado: {}'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>b and c>a:
    maior = c
print('o maior valor digitado: {}'.format(maior))