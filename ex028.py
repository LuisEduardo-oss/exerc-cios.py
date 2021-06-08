import random
n = int(input('digite um numero:'))
n1 = random.choice([0,5])
if n == n1:
    print('voce acertou, PARABENS')
else:
    print('voce errou:/')
print('o numero era {}'.format(n1))
