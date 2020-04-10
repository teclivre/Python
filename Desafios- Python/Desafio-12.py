# Preço do produto com desconto.
print ('Agora temos desconto em todos os produtos.\n \n')

price = float (input('Fale o valor do produto que deseja desconto: '))

discount = price * 0.05
value = price - discount

print('Esse produto custa R${:.2f} e com desconto de 5% Custará R${:.2f}.\n \n'.format(price,value))