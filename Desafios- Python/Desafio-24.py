print('\n\n Vamos avaliar se sua cidade começa com Santo. \n')
city = str(input ('Digite sua cidade: ')).strip()
cit = city[:5].capitalize() == 'Santo'
print(cit)
#print ('Santo' in cit)    