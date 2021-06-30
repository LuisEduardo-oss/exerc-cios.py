from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('em qual ano você nasceu? '))
idade = date.today().year - ano_nasc
print('quem nasceu em {} tem {} anos em {}'.format(ano_nasc,idade,ano_atual))
if idade == 18:
    print('voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    print('voce ainda nao tem idade para se alistar')
    saldo = 18 - idade
    print('ainda falta {} anos para voce se alistar'.format(saldo))
elif idade > 18:
    print('ja passou da hora de voce se alistar')
    saldo = idade - 18
    print('voce deveria ter se alistado a {} anos'.format(saldo))