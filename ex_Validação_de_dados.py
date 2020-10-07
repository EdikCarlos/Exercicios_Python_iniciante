sexo = str(input('Informe seu sexo: [M/F]: ')).upper()[0].strip()
while sexo not in 'MF':
    print('Dados inválidos, tente novamente')
    sexo = str(input('Informe seu sexo: [M/F]: ')).upper().strip()
print('Dados registrados com sucesso!')