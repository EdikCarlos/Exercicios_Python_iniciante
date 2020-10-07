valor = int(input('Quanto deseja sacar?R$'))
totced = 0
ced = 50
total = valor
while True:
    if ced <= total:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédula(s) de R${ced}.')
        totced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        elif total == 0:
            break

