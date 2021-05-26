dias = int(input('quantos dias o carro foi alugado? '))
km = int(input('quantos km o carro rodou? '))
valor = dias * 60
kms = km * 0.15
vt = valor + kms
print('o valor a pagar pelo carro é R${:.2f}'.format(vt))