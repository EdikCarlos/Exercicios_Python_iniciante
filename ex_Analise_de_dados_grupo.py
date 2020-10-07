maior_18 = 0
homens = 0
mulher_menor = 0
while True:
    print('=-'*25)
    idade = int(input('Digite a idade:'))
    sexo = str(input('Qual o sexo [M/F]:')).upper().strip()
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if idade > 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    if resp == 'N':
        break
print('=-'*25)
print('FIM DO PROGRAMA, OS RESULTADOS FORAM:')
print(f'''Foram cadastradas {maior_18} pessoas maiores de 18 anos.
Foram cadastrados {homens} homens.
Foram cadastradas {mulher_menor} mulheres com menos de 20 anos.''')