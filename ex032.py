from datetime import date
ano = int(input('qual ano quer analisar? coloque 0 se quiser analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano de {} é BISSEXTO'.format(ano))
else:
    print('o ano de {} não é BISSEXTO'.format(ano))