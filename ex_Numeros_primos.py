n = int(input('Digite um número para saber se ele é primo :'))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end=' ')
        div = div + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n,div))
if div == 2:
    print('Portanto o número {} é PRIMO!!!'.format(n))
else:
    print('Portanto o número {} NÃO É PRIMO!!!'.format((n)))