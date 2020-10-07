n = int(input('Digite um número inteiro para ver o valor de seu fatorial: '))
f = 1
while n > 0:
    print('{} '.format(n),end='')
    print('x ' if n > 1 else '= ',end= '')
    f = f * n
    n = n - 1
print(f)



