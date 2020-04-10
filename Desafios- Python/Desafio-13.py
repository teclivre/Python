# Reajuste de saĺário

salary = float (input('\n \n Diga seu salário: R$'))
percentage = float (input('Qual a podentagem: '))

readjustment = salary*(percentage/100)
total = readjustment + salary


print('O seu salário hoje é R${:.2f} e com {:.0f}% de aumento, passará a ser R${:.2f}. \n \n '.format(salary,percentage,total) )
