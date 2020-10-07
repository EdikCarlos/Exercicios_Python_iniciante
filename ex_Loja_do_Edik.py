print('=-'*15)
print('LOJAS EDIK CARLOS')
print('=-'*15)
valor = float(input('Digite o valor total das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque.
[2] à vista no cartão.
[3] 2x no cartão.
[4] 3x ou mais no cartão.''')
opção = int(input('Qual a sua opção?: '))
if opção == 1:
    print('O valor das compras ficará em R${:.2f} com o desconto.'.format(valor - (valor * 10/100)))
elif opção == 2:
    print('O valor das compras ficará em R${:.2f} com o desconto.'.format(valor - (valor * 5/100)))
elif opção == 3:
    parcela = valor / 2
    print ('O valor a pagar será R${:.2f} parcelado em 2x de R${:.2f}.'.format(valor, parcela))
elif opção == 4:
    vezes = int(input('Quantas parcelas serão?: '))
    valor = valor + (valor * 20/100)
    parcela = valor / vezes
    print ('O valor com juros ficará R${:.2f} e serão {} parcelas no valor de R${:.2f}.'.format(valor, vezes, parcela))
else:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m')