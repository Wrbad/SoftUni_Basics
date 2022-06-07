from math import pi

figure = str(input())
lenght = float(input())

if figure == 'square':
    print(f'{(lenght * lenght):.3f}')

elif figure == 'rectangle':
    height = float(input())
    print(f'{(lenght * height):.3f}')

elif figure == 'circle':
    print(f'{(lenght * lenght * pi):.3f}')

elif figure == 'triangle':
    height = float(input())
    print(f'{(lenght * height * 0.5):.3f}')