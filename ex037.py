num = int(input('digite um numero inteiro? '))
print('escolha uma base de converções:\n'
      '[ 1 ] converter em BINARIO\n'
      '[ 2 ] converter em OCTAL\n'
      '[ 3 ] converter em hexadecimal')
opção = int(input('qual a sua opção? '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual {}'.format(num, hex(num)[2:]))
else:
    print('opção inválida ')