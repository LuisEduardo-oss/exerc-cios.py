r = float(input('quanto dinheiro voce tem na carteira? R$'))
d = r / 5.33
e = r / 6.53
print('com {}R$ você consegue comprar {:.2f}US$'.format(r, d))
print('com {}R$ você consegue comprar {:.2f}EUR'.format(r, e))