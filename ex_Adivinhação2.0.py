from random import randint
from time import sleep
jogador = int(input('Irei pensar em um número de 0 a 10, qual você acredita que será? :'))
print('\033[35m-=-\033[m' * 8)
print('\033[7:35:40mPROCESSANDO...\033[m')
print('\033[35m-=-\033[m' * 8)
sleep(3)
pc = randint(0,10)
resposta = jogador == pc
palpites = 1
while jogador != resposta:
    jogador = int(input('Errou! Tente novamente: '))
    print('\033[35m-=-\033[m' * 8)
    print('\033[7:35:40mPROCESSANDO...\033[m')
    print('\033[35m-=-\033[m' * 8)
    sleep(3)
    palpites += 1
print('Você acertou e necessitou de {} palpites.'.format(palpites))