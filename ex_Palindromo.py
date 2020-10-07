nome = str(input('Digite alguma palavra ou frase :')).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(junto, inverso)
if junto == inverso:
    print('A palavra/frase \033[36m{}\033[m É UM PALÍNDROMO.'.format(nome))
else:
    print('A palavra/frase \033[36m{}\033[m NÃO É UM PALÍNDROMO.'.format(nome))