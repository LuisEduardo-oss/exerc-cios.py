pre = float(input('qual o valor do produto?R$ '))
pro = int(str(input('quantos % vai ser o desconto?')))
des = pre - (pre * pro / 100)
print('o produto custava {}R$ com o desconto de {}% vai custar {}R$'.format(pre, pro, des))
