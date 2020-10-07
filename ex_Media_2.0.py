n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
if media < 5:
    print('O aluno obteve uma média {:.2f}, sendo assim está \033[31mREPROVADO\033[m.'.format(media))
elif 5 <= media <= 6.9:
    print('O aluno obteve uma média {:.2f}, sendo assim está de \033[33mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('O aluno obteve uma média {:.2f}, sendo assim está \033[32mAPROVADO\033[m.'.format(media))
