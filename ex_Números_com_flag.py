cont = 0
soma = 0
while True:
    n = int(input('Digite um número para somá-lo (Digite 999 para parar o programa): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números e a soma deles foi {soma}.')