#Agora vamos medir quantos metros quadrados te uma parede e a quantidade de tinta para pinta-la.

width = float (input(' \n Me diga largura da parede: '))
height = float(input('Agora me diga a altura da parede: '))

meter = width*height
ink =  meter*2

print('Sua parede tem {:.2f}x{:.2f} e têm {:.2f}m² e para pinta-la você usará {:.2f}l de tinta. \n \n'.format(width,height, meter,ink))
