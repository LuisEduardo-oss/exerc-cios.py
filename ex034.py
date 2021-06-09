sal = float(input('qual o salario do funcionario? R$'))
if sal < 1250.00:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('quam ganhava R${:.2f} vai passar a ganhar R${:.2f}'.format(sal, novo))
