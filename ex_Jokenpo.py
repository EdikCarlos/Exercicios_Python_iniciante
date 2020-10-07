from random import randint
from time import sleep
lista = (' ', 'PEDRA', 'PAPEL', 'TESOURA')
escolha_cpu = randint(1,3)
print('''FAÇA SUA ESCOLHA
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
escolha_jogador = int(input('Qual será sua jogada?: '))
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO')
print('-='*14)
print('O jogador jogou {}.'.format(lista[escolha_jogador]))
print('O computador jogou {}.'.format(lista[escolha_cpu]))
print('-='*14)
if escolha_jogador == 0:
    print('OPÇÂO INVÁLIDA.')
elif escolha_cpu == 1: #Pedra
    if escolha_jogador == 1:
        print('DEU EMPATE.')
    elif escolha_jogador == 2:
        print('SHOW! VOCÊ VENCEU!')
    elif escolha_jogador == 3:
        print('HAHAHA VOCÊ PERDEU.')
    else:
        print('OPÇÃO INVÁLIDA.')
elif escolha_cpu == 2: #Papel
    if escolha_jogador == 1:
        print('HAHAHA VOCÊ PERDEU.')
    elif escolha_jogador == 2:
        print('DEU EMPATE.')
    elif escolha_jogador == 3:
        print('SHOW! VOCÊ VENCEU!')
    else:
        print('OPÇÃO INVÁLIDA.')
elif escolha_cpu == 3: #Tesoura
    if escolha_jogador == 1:
        print('SHOW! VOCÊ VENCEU!')
    elif escolha_jogador == 2:
        print('HAHAHA VOCÊ PERDEU.')
    elif escolha_jogador == 3:
        print('DEU EMPATE.')
    else:
        print('OPÇÃO INVÁLIDA')
