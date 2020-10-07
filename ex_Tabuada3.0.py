while True:
    n = int(input('Digite um número para ver sua tabuada (Digite 0 para finalizar): '))
    print('-='*20)
    if n == 0:
        break
    for c in range(1, 11):
        mult = n * c
        print(f'{n} x {c} = {mult}' )
    print('-=' * 20)
print('\033[33mPrograma finalizado com sucesso! Obrigado por usar.\033[m')