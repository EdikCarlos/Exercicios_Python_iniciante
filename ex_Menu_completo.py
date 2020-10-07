n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
escolha = -1
soma = 0
prod = 0
while escolha != 5:
    print('=-*'*20)
    print('''ESCOLHA:
[1] Somar
[2] Multiplicar
[3] Mostrar o maior
[4] Escolher outros valores
[5] Sair do programa''')
    escolha = int(input('>>>>> Qual a sua opção?: '))
    print('=-*' * 20)
    if escolha == 1:
        soma = n1 + n2
        print('\033[33m{} + {} = {}.\033[m'.format(n1, n2, soma))
    if escolha == 2:
        prod = n1 * n2
        print('\033[33m{} x {} = {}.\033[m'.format(n1, n2, prod))
    if escolha == 3:
        if n1 > n2:
            print('\033[33mO maior número foi {}.\033[m'.format(n1))
        elif n2 > n1:
            print('\033[33mO maior número foi {}.\033[m'.format(n2))
        elif n1 == n2:
            print('\033[33mSão Iguais\033[m')
    if escolha == 4:
        n1 = int(input('Faça sua primeira nova escolha: '))
        n2 = int(input('Faça sua segunda nova escolha: '))
print('\033[35mFIM DO PROGRAMA, OBRIGADO POR USAR!\033[m')

