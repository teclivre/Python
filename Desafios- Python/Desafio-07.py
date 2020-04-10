print ('Cálculo de médias de notas: \n \n \n')

student  = input ('Digite o nome do aluno: ')

n1  = float (input('Digite a primeira nota: '))
n2 =  float (input('Digite a segunda nota: '))

print ('Primeira nota: {} \n Segunda nota: {}'.format(n1,n2))

average = (n1+n2)/2

print ('A média das nota de {} é {:0.2f}.'.format(student,average))