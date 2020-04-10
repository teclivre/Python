print ('\n\n ')
name = str (input('Digite Seu nome completo: ' )).strip()
n = name.upper()
print('Seu nome é {}'.format(n))
print('Seu nome tem SILVA? {}'.format('SILVA' in n))
print('SILVA' in n)

print('\n\n')
print(name.capitalize())