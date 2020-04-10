from math import hypot

catad = float (input('\n\n Informe o valor do cateto adjacente: '))
catop = float (input('Informe o valor do cateto oposto: '))

hypotenuse = hypot(catop, catad)

print ('O cumprimento da hipotenusa é:{:.2f}' .format(hypotenuse))
