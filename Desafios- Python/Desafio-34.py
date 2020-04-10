print('\n\n Cálculo de aumento de salário. \n\n')

salary = float (input('Diga o seu salário para calculamos o valor do aumento: R$'))
s10 = salary + (salary*0.10)
s15 = salary + (salary*0.15)

if salary > 1250.00:
    print('Seu salário hoje é R${:.2f} e parrara a ser R${:.2f}, após o aumento.'.format(salary, s10))
else:
    print('Seu salário hoje é R${:.2f} e passará a ser R${:.2f} após o aumento. \n\n'.format(salary,s15))    
