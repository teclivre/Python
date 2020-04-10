import math
print('\n')
print('-=-'*10)
number = int(input('Digite um número: '))
print('-=-'*10)

odd = number % 2
if odd == 0:
    print ('o número {} é par.'.format(number))
else:
    print ('O número {} é Impar.'.format(number)) 
print('-=-'*5)    
print('Fim.')       
print('-=-'*5)
