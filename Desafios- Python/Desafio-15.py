# Aluguel de caros.
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado #
# e a quantidade de dias pelos quais ele foi alugado. #
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


print('\n \n\ A diaria é R$60 + R$0,15/km')
kilometer = float (input('Quantos kilometros você rodou? '))
day = float(input('Quantos dias você ficou com o caro?'))

km = kilometer*0.15
diaria = day*60

print('Você irá pagar R${:.2f} pela kilometragem rodada e R${:.2f} pelas diarias, Totalizando R${:.2f}'.format(km,diaria,km+diaria))
