from random import randint
from time import sleep
soma = 0
while True:
    print(('-='*25))
    print('''Escolha uma opção:
    [0] PAR
    [1] ÍMPAR''')
    escolha = int(input('Sua opção: '))
    ncpu = randint(0, 9)
    nj = int(input('Escolha um número: '))
    print('Escolha do computador',ncpu)
    par = (nj + ncpu) % 2 == 0
    impar = (nj + ncpu) % 2 == 1
    if escolha == 0:
        if par:
            print('DEU PAR! VOCÊ VENCEU!')
            soma += 1
        elif impar:
            print('DEU ÍMPAR! VOCÊ PERDEU!')
            break
    elif escolha == 1:
        if impar:
            print('DEU ÍMPAR! VOCÊ VENCEU!')
            soma += 1
        elif par:
            print('DEU PAR! VOCÊ PERDEU!')
            break
    print('-='*25)
print(f'GAME OVER! Você venceu {soma} vezes seguidas. ')




