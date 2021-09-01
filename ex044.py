print('=' * 10, end='')
print('Loja Luizão', end='')
print('=' * 10)
valor = float(input('Valor das compras: R$'))
print('''FORMAS DE PAGAMENTO:
        [ 1 ] À vista dinheiro/cheque
        [ 2 ] À vista cartão
        [ 3 ] 2x no cartão
        [ 4 ] 3x ou mais no cartão''')
opção = int(input('qual é a opção? '))
if opção == 1:
    desconto = valor - (valor * 10 / 100)
    print('sua compra de R${:.2f} foi para R${:.2f}'.format(valor, desconto))
elif opção == 2:
    desconto = valor - (valor * 5 / 100)
    print('sua compra de R${:.2f} foi para R${:.2f}'.format(valor, desconto))
elif opção == 3:
    print('sua compra sai pelo valor normal: R${:.2f}'.format(valor))
elif opção == 4:
    var = valor + (valor * 20 / 100)
    parcelas = int(input('quantas parcelas?'))
    divisao = var / parcelas
    print('sua compra sera parcelada em {:.2f}x de R${:.2f} COM JUROS '.format(parcelas, divisao))
    print('sua compra de R${:.2f} vai custar R${:.2f}'.format(valor, var))