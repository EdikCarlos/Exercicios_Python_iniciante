from datetime import date
ano_atual = date.today().year
menor = 0
maior = 0
for c in range(1,8):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa?: '.format(c)))
    idade = ano_atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('''A quantidade de pessoas na maioridade são {}.
A quantidade de pessoas de menor são {}.'''.format(maior, menor))