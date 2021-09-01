from random import randint
print('{}{}{}'.format(('=' * 10), 'JOKENPÔ', ('=' * 10)))
itens = 'pedra', 'papel', 'tesoura'
computador = randint(0, 2)
print('SUAS OPÇÕES:'
      '[ O ] PEDRA'
      '[ 1 ] PAPEL'
      '[ 2 ] TESOURA')
jogador = int(input('qual a sua jogada? '))
print('-=' * 10)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)
if computador == 0:  #computador jogou pedra
    if jogador == 0:
        print('JOGO EMPATADO')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    else:
        print('COMPUTADOR VENDEU')
elif computador == 1: #computador jogou papel
    if jogador == 1:
        print('JOGO EMPATADO')
    elif jogador == 0:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADOR VENCEU')
elif computador == 2: # computador jogou tesoura
    if jogador == 2:
        print('JOGO EMPATADO')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADDOR VENCEU')