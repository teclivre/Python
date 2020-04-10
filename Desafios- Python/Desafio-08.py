# Calculation of meter to centimeter and millimeter conversion.

print ('Conversão de metros para centimetro e milimetro. \n \n')

name = input ('Qual o seu nome? ')



print ('\n \n Olá {}, qual o valor que deseja converter? \n '.format(name))
meter = float (input('Digite aqui: '))
centimeter = meter * 100
millimeter = meter * 1000
kilometer = meter / 1000
decimeter = meter / 10

print ('\n \n {}m é o valor escolhido.\n \n Equivale a {:.0f}cm ou {:.0f}mm.\n \n'.format(meter,centimeter,millimeter))
print('\n \n O valor escolho é {}. \n equivale a {}km ou {}dm. \n \n'.format(meter,kilometer,decimeter))