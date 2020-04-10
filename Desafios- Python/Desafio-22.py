print('\n\n')
name = str (input('Digite seu nome completo: ')).strip()
print('\n\n')
print('Seu nome com todas as letra maiusculas: {} ' .format(name.upper()))
print('Seu nome com todas as letra minúsculas: {}'.format(name.lower()))
print('Seu nome tem {} letras.'.format(len(name) - name.count(' ')))
divided = name.split()
#Modo que eu fiz.
#print('Seu primeiro nome é {} e tem {}'.format(divided[0], name.find(' ')))
# Também pode ser feito com o len
print ('Seu primeiro nome é {} e ele tem {} letras.'.format(divided[0].capitalize(), len(divided[0])))


print('\n\n')