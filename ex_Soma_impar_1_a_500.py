soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A quantidade de números ímpares entre 1 e 500 divisíveis por três é {} e a soma desses número é {}.'.format(cont, soma))