#cadeia de texto, como manilular os textos.

frase = ('Roberio Luis Figueiredo da Silva')
minuscula =('aline naiany rodrigues ferreira')
espaco = ('   Aline Naiany Rodrigues Ferreira   ')

#Fatiamento

print(frase[0])
print(frase[:12:2])
print(frase[1:])

print(len(frase))
print('\n\n\n')
print(frase.count('o',0,8))

print(frase[::3])


print(len(frase))
#imprimir as letra r da frase
print(frase.count('r'))

#mosta one começa o Silva
print(frase.find('Silva'))
print('\n\n')
print(frase.find('ALine'))

print('\n\n')
#Troca Roberio Por ALine
print(frase.replace('Roberio','Aline'))

#Todas as Letras ficam maiusculas
print(frase.upper())
#Todas as Letras ficam minusculas
print(frase.lower())
#somente a primeira fica maiuscula
print(minuscula.capitalize())
##limina todos os espaços
print(espaco.strip())
#O 'r' Elimina apenas os espaços da direita
print(espaco.rstrip())
#elimina o espaço da esqueda
print(espaco.lstrip())
#Separa a frase 
print(frase.split())
#Junta as frase
print('-'.join(frase))
print('\n\n\n')
#Coloca-se ''' para escrever textos longos
print('''Over the last decade we have witnessed the emergence of technologies such as libraries, Object Orientation, software architecture
and visual programming. The common goal of these technologies is to achieve software reuse. Even though, many significant
advances have been made in areas such as library design, domain analysis, metric of reuse and organization for reuse, there are still
unresolved problems such as component inter-operability and framework design[1]. We have investigated the use of interpreted languages to create a programmable, dynamic environment in which components can be tied together at a high level. This work has
demonstrated the benefits of such an approach and has taught us about the features of the interpreted language that are key to a successful component integration.''')

print('\n\n')
print('Roberio' in frase)

print('\n')