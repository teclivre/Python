

color = { 'yelow':' \033[33m',
        'clear':' \033[m',}

print('\33[1;30;41m Olá mundo! \33[m')

print('\33[1;30;44m Olá mundo! \33[m')

print('Olá,{}{}{} '.format(color['yelow'],'Roberio',color['clear']))
