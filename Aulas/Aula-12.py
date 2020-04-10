print('\33[1;34m --=--\33[m'*9)
print('\33[1;30;43m Conteúdo da Aula 12\33[m \33[1;4;31m Condições Aninhadas.\33[m ')
print('\33[1;34m --=--\33[m'*9)
print('\n')
color = {'White': '\33[1;30m',
          'Red': '\33[1;31m'}


n = str( input(' \33[1;36m Qual é seu nome? \33[m '))
n1 = n.strip()
name = n1.capitalize()
if name == 'Roberio':
    print(f"\33[1;31m Que nome lindo!, {name} \33[m")
elif name == 'Pedro' or name == 'Maria' or name == 'Creuza':
    print('\33[1;31mSeu nome é normal, {}!!!\33[m'.format(name))
elif name == 'Aline' or name == 'Mel':
    print(f'\33[1;35m Eu te Amo, {name}! \33[m')
else: print(f'Seu nome é normal no Brasil {name}.')
print('Tenha um bom dia, {}!'.format(name))
