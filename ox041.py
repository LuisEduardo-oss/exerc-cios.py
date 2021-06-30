from datetime import date
ano_nasc = int(input('ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print('o atleta tem {} anos'.format(idade))
if idade <= 9:
    print('classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('classificação: JUNIOR')
elif idade == 20:
    print('classificação: SÊNIOR')
elif idade > 20:
    print('calssificacão: MASTER')
