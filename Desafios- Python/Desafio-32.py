from datetime import date

print('\n')

year = int (input('Digite o ano para saber se é bissexto, se dititar 0 será o anoo da máquina: '))
if year == 0 :
    year = date.today().year
if year%4 == 0 and year%100!= 0 or year%400==0:
    print('{} é ano bissexto.'.format(year))
else:
    print('{} não é ano bissexto.'.format(year))    