n = int(input('Qual o primeiro termo da PA?: '))
r = int(input('Qual a razão da PA?: '))
cont = 10
while cont > 0:
    print(n,'--> ',end='')
    n += r
    cont -= 1
print('FIM')