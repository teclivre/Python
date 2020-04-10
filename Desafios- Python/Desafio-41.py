print('\33[1;30;44m Desafio 41 \33[m')
print('\n')

'''A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um 
atleta e mostre sua categoria, de acordo com a idade

- Até 9 anos: Mirim
- Até 14 anos: infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master'''

from datetime import date

year = int(input('Digite o ano de nascimento do altela: '))

age = date.today().year - year

if age <= 9:
    print('\33[1;31m Categoria MIRIM.\33[m')
elif age > 9 and  age <= 14:
    print('\33[1;31m Categoria INFANTIL.\33[m')
elif age > 14 and age < 19:
    print('\33[1;31m Categoria JUNIOR.\33[m')
elif age == 20:
    print('\33[1;31m Categoria SÊNIOR.\33[m')
elif age > 20:
    print('\33[1;31m Categoria MASTER.\33[m')

print("\n FIM!")

