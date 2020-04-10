import math 
print('\n\n \33[0;33;31mVocê irá digitar três números e iremos te mostar o maior e o menor.\33[m\n')

n1 = int (input(' \33[1;30m Digite o primeiro número:\33[m '))
n2 = int (input('\33[1;30m Digite o segundo número:\33[m '))
n3 = int (input('\33[1;30m Digite o terceiro número:\33[m '))

# Analizando o menor número.
smaller = n1
if n2<n1 and n2<n3:
    smaller = n2
if n3<n1 and n3<n2:
    smaller = n3    
print('\n O número menor é {}'.format(smaller))                         

bigger = n1
if n2 >n1 and n2>n3:
    bigger = n2
if n3>n1 and n3>n2:
    bigger = n3
print('O maior número é: {}'.format(bigger))        
