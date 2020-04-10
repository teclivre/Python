from random import shuffle

print('\n\n')

a1 = str (input('Primeiro aluno: '))
a2 = str (input('Segundo aluno: '))
a3 = str (input('terceiro Aluno: '))
a4 = str (input('Quarto Aluno: '))
a5 = str (input('Quinto Aluno: '))

List = [a1,a2,a3,a4,a5]
shuffle(List)

print('A Ordem do Sorteio é:')
print(List)