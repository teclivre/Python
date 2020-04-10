from math import sin, cos, tan,radians

a = float(input('\n\n Informe um ângulo: '))

sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))

print('\n\n O ângulo escolhido é: {:.3f}'.format(a) )
print('\n\n\n O seno de {:.3f} é: {:.3f}'.format(a, sen))
print('O cosseno de {:.3f} é: {:.3f}'.format(a, cos))
print('A tangente de {:.3f} é: {:.3f}\n\n\n'.format(a, tan))
