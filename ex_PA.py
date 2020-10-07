n = int(input('Qual o primeiro termo da PA?: '))
r = int(input('Qual a razão da PA?: '))
soma = n
for c in range(1,11):
    print(soma, end=' -> ')
    soma += r
print('FIM')