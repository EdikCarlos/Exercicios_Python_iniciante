peso = float(input('Qual o seu peso em Kg? :'))
altura = float(input('Qual sua altura? :'))
imc = peso / altura**2
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso, procure um nutricionista.')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você esta no seu peso ideal, continue assim!')
elif imc >= 25 and imc < 30:
    print('Fique atento, você esta com SOBREPESO.')
elif imc >= 30 and imc < 40:
    print('CUIDADO! Você está OBESO, procure um nutricionista para não ter problemas piores!')
else:
    print('PERIGO!VOCÊ ESTA COM OBESIDADE MÓRBIDA, PROCURE UM MÉDICO ANTES QUE SEJA TARDE.')