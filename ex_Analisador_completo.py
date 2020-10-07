somaidade = 0
hvelho = ''
maior = 0
mm20 = 0
print('TEM QUE HAVER AO MENOS UM HOMEM E UMA MULHER.')
for c in range(1,5):
    print('----- DADOS DA {}ª PESSOA -----'.format(c))
    nome = str(input('Qual o nome da pessoa: ')).strip()
    idade = int(input('Qual a idade da pessoa: '))
    sexo = str(input('Qual o sexo [M/F]: ')).strip().upper()
    somaidade += idade
    media = somaidade / 4
    if sexo == 'M' and idade > maior:
        maior = idade
        hvelho = nome
    if sexo == 'F' and idade < 20:
        mm20 += 1
print('-='*35)
print('A media de idade entre todas as pessoas é {:.0f} anos'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(hvelho, maior))
print('O número de mulheres menores de 20 anos é {}'.format(mm20))
