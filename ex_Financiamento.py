valor = float(input('Valor da casa: R$'))
salario = float(input('Valor do salário: R$'))
tempo = int(input('Quantos anos de prestação?: '))
ano = tempo * 12
prestação = valor/ano
if prestação > salario * 30/100:
    print('\033[31mNEGADO\033[m')
    print('Seriam {} anos com uma prestação mensal de R${:.2f}, infelizmente o seu salário de R${:.2f} NÃO É COMPATÍVEL!'.format(tempo, prestação, salario))
else:
    print('\033[32mAUTORIZADO\033[m')
    print('Serão {} com uma prestação mensal de R${:.2f}'.format(tempo, prestação))