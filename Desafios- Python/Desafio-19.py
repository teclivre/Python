from random import choice

print('\n\n')
a1 = str (input ('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto aluno: '))
a5 = str (input('Quinto aluno: '))

#s = random.choice[a1,a2,a3,a4,a5]

print('\n\nO ganhador é: {}\n\n'.format(choice([a1, a2, a3, a4, a5])))