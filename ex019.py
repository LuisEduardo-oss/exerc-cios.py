import random
n1 = input('qual o primeiro aluno? ')
n2 = input('qual o segundo aluno? ')
n3 = input('qual o terceiro aluno? ')
n4 = input('qual o quarto aluno? ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('o aluno escolhido foi:{}'.format(escolhido))