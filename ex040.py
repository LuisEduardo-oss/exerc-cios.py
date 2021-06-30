n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1 + n2) / 2
print('a média entra {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))
if media >= 7:
    print('o aluno esta APROVADO')
elif media <=7 and media >= 5:
    print('o aluno esta de RECUPERAÇÃO')
elif media < 5:
    print('o aluno esta REPROVADO')