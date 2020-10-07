maior = 0
menor = 9999
for c in range(1,6):
    print('-='*20)
    print('DADOS DA {}ª PESSOA:'.format(c))
    peso = float(input('Qual o peso: '))
    print('-='*20)
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('''O maior peso foi {}Kg.
O menor peso foi {}Kg'''.format(maior, menor))