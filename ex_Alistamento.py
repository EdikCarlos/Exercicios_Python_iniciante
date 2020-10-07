nasc = int(input('Qual seu ano de nascimento: '))
from datetime import date
ano_atual = date.today().year
idade = ano_atual - nasc
falta = 18 - idade
passou = idade - 18
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano_atual))
if idade < 18:
    print('Ainda faltam {} anos para você se apresentar para o alistamento.'.format(falta))
    print('Seu alistamento será em {}.'.format(ano_atual + falta))
elif idade > 18:
    print('Já se passaram {} anos da data do seu alistamento que foi em {}.'.format(passou, ano_atual - passou))
else:
    print('Você tem 18 anos, está na hora de se apresentar, boa sorte!!!')