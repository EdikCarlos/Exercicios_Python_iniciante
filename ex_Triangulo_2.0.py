l1 = float(input('Digite a primeira medida: '))
l2 = float(input('Digite a segunda medida: '))
l3 = float(input('Digite a terceira medida: '))
real = (l2 - l3) < l1 < l2 + l3 and (l1 - l3) < l2 < l1 + l3 and (l1 - l2) < l3 < l1 + l2
if real and l1 == l2 == l3:
    print('O triângulo será do tipo EQUILATERO.')
elif real and l1 != l2 != l3 != l1:
    print('O triangulo será do tipo ESCALENO.')
elif real and l1 == l2 != l3 or l2 == l3 != l1 or l3 == l1 != l2:
    print('O triangulo será do tipo ISÓSCELES.')
else:
    print('\033[31mNÃO É POSSÍVEL FAZER UM TRIÂNGULO COM ESSAS MEDIAS!\033[m')