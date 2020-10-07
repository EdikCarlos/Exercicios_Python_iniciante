from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano
print('A sua idade é {} anos'.format(idade))
if idade <= 9:
    print('A sua categoria é MIRIM.')
elif 9 < idade <= 14:
    print('A sua categoria é INFANTIL.')
elif 14 < idade <= 19:
    print('A sua categoria é JUNIOR.')
elif 19 < idade <= 25:
    print('A sua categoria é SÊNIOR.')
else:
    print('A sua categoria é MASTER.')