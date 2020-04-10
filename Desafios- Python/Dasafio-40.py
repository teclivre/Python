print('\n\33[1;30;45m desafio 40 \33[m')
print('\n')

'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma 
mensagem no final, de acordo com dua média

- Média abaixo de 5.0:
 Reprovado
 -Média entre 5.0 e 6.9:
 Recuperação.
 - Média superior a 7.0:
 Aprovado
 
'''
name = str(input('Diga seu nome: '))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua Segunda nota: '))
n = name.upper()
average = (n1 + n2)/2
if average < 5.0:
    print(f'{n}, sua média é {average} e você está REPROVADO.')
elif average >= 5.0 and average < 6.9:
    print(f'{n}, sua média é {average :0.2f}, RECUPERAÇÃO.')
elif average >= 7.0:
    print(f'{n}, sua média é{average :0.2f} e você está aprovado, PARABÉNS!\n')
