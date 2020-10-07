soma = 0
n = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [Digite 999 para parar]: '))
    if n == 999:
        soma -= 999
        cont -= 1
    soma += n
    cont += 1
print('Você digitou {} números e a soma deles foi {}.'.format(cont, soma))
print('Fim')