casa = float(input('qual o valor da casa? R$'))
salario = float(input('qual o seu salario? R$'))
anos = int(input('em quantos anos voce vai pagar? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
if prestação <= minimo:
    print('emprestimo pode ser CONCEDIDO')
else:
    print('emprestimo NEGADO')