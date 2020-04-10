print('Vamos fazer alguns testes agora!')

n1 =  int (input('Digite um número: '))
n2 =  int (input('Digite outro número: '))

s = n1 + n2
sub = n1 - n2
d = n1 / n2

pot = n1**n2
di = n1 // n2
# A barra invertida é para quebra a linha em um mesmo print.
print ('A soma dos números é:  {} \n Asubtração dos números é: {} \n A divisão dos números é: {:.4f} \n A Divisão inteira dos números é: {} '.format(s,sub,d, di))
print ('A Potências dos número é: {}'.format(pot))


print('\n \n Outros exemplos: ')
# O end= é para que a linha não seja quebrada.
print('\n A soma é: {}' .format(s), end='>>> ')
print('A Potência é: {}'.format(pot))