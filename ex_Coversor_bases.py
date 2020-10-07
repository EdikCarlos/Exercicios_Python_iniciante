n = int(input('Digite um número inteiro para convertê-lo: '))
print('''Escolha uma das opções de bases a seguir a seguir:
[1] Converter em BINÁRIO
[2] Converter em OCTAL
[3] Converter em HEXADECIMAL''')
opção = int(input('Qual a sua opção?: '))
if opção == 1 :
    print('O número {} em base BINÁRIA será {}.'.format(n, bin(n)[2:]))
elif opção == 2:
    print('O número {} em base OCTAL será {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('O número {} em base HEXADECIMAL será {}'.format(n, hex(n)[2:]))
else:
    print('\033[31mOpção inválida, tente novamente.\033[m')