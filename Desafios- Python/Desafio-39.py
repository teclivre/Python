from datetime import date
print('\33[1:30:44m Desafio 39 \33[m')

'''Faça um programa que leia o ano de nascimento de um jovem e informe , de acordo 
com sua idade:
- Se ele vai se alistar ao serviço militar.
- Se ja está na hora de se alistar.
- Se ja passou do tempo de alistamento.

Também deve mostrar o tempo que falata ou ja passou do prazo.'''

name = str(input('Escreva seu nome completo: '))
year = int(input('Escreva o ano de seu nascimento: '))
genre1 = str(input('Informe seu Genero, M/F: '))
n = name.upper()
genre = genre1.upper()
age = date.today().year - year
age1 = year + 18
age2 =  age1 - date.today().year
M = 'Masculino'
F = 'Feminino'
print(f'{n}, você tem {age} anos.')
if genre == 'M':
    print(f'{n}, Seu genero é {M}')
    if age == 18:
       print(f'{n}, você está no ano de alistamento.')
    elif age > 18:
       print(f'{n}, você passou do tempo para se alistar em {date.today().year- age1} anos. ')
    elif age < 18:
       print(f'{n}, você ainda não está no tempo de se alistar, faltam {age2} anos')
else:
    print(f'{n}, Se Genero é {F} e você não precisa se alistar.')
print('\n')
print(f'Tenha um ótimo dia, {n}!')

