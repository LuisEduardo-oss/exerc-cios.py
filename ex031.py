dis = int(input('qual a distancia em km da viagem? '))
print('voce esta preste a embarcar em uma viagem de {}km'.format(dis))
if dis < 200:
    valor = dis * 0.50
    print('o valor do passagem sera: R${:.2f}'.format(valor))
else:
    valor = dis * 0.45
    print('o valor da passagem sera R${:.2f}'.format(valor))
