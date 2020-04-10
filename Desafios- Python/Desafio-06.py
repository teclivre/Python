print('Exercicio 05.2 \n')

#('Criando um algoritmo que leia um número e mostre o seu dobro, triplo e a sua raiz quadrada.')

n = int (input ('Digite um número: ' ))

d = n*2
t = n*3
r2 = n**(0.5)

print('O número escolhido é: {} \n \n O dobro é: {} \n O triplo é: {}, \n A Raiz quadrada é: {:0.3f}' .format(n,d,t,r2))