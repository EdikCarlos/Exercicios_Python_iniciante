total = 0
prodmaisdemil = 0
barato = ''
menor = 999999999
while True:
    nome = str(input('Qual o produto:')).upper().strip()
    preco = float(input('Qual o preço:R$'))
    total += preco
    resp = str(input('Gostaria de continuar? [S/N]:')).upper().strip()
    while resp != 'S' and resp != 'N':
        resp = str(input('Gostaria de continuar? [S/N]:')).upper().strip()
    if preco > 1000:
        prodmaisdemil += 1
    if preco < menor:
        menor = preco
        barato = nome
    if resp == 'N':
        break
print(f'''O total gasto na compra foi R${total:.2f}.
O total de produtos que custam mais de R$1000.00 foram {prodmaisdemil}.
O produto mais barato foi {barato}.''')
