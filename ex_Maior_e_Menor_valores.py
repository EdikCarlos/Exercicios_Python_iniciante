escolha = 'S'
soma = 0
maior = 0
cont = 0
menor = 9999
media = 0
while escolha == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    escolha = str(input('Gostaria de continuar? [S/N]: ')).upper()
    if n > maior:
        maior = n
    if n < menor:
        menor = n
media = soma / cont
print('Você digitou {} números e a média entre eles foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))