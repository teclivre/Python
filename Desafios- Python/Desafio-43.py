print('-=-'*24)
print('\33[30;44m Desafio 43 \33[m')
print('\n\n')

Weight = float(input('Ditite seu peso: (Kg) '))
height = float(input('Digite sua altura: (M) '))

imc = Weight / (height ** 2)

#print(f'')

if imc < 18.4:
    print(f'Seu IMC está {imc :0.2f} e você está abaixo do peso IDEAL.')
    print('Alimente-se mais.')
elif imc >= 18.4 and imc < 25:
    print(f'Seu IMC está {imc :0.2f} e você está no seu peso IDEAL')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC está {imc :0.2f} e você está acima do seu peso IDEAL, com SOBREPESO.')
elif imc >= 30 and imc < 35:
    print(f'Seu IMC está {imc :0.2f} e você está acima do seu peso IDEAL, com OBESIDADE GRAU 1.')
elif imc >= 35 and imc < 40:
    print(f'Seu IMC está {imc :0.2f} e você está acima do peso IDEAL, com OBEISIDADE GRAU 2.')
elif imc >= 40:
    print(f'Seu IMC está {imc :0.2f} e você está acima do peso IDEAL, com OBESIDADE grau 3.')

print('-=-'*24)
