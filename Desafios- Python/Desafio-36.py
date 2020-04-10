print ('\33[1;31m Desafio 36 \33[m')
print('\n')
print('\33[1;36;40m Vamos tentar simular o seu emprestimo.\33[m')

name = str(input('Informe seu nome completo: '))
salary = float(input('Informe Seu salário: R$'))
value = float(input('Informe o Valor do Imível: R$'))
months = int(input('Informe o período em meses: '))
n = name.strip()

monthly = value/months
salary1 = salary * 30/100

if monthly <= salary1:
    print(f'Seu Empréstimo está aprovado, {n.capitalize()}.')
elif monthly > salary1:
    print(f'Empréstimo não aprovado, pois, ultrapassa 30% de seu Salário, {n.capitalize()}.')

print(f'Tenha um bom dia, {n.capitalize()}!')



