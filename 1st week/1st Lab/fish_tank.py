lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())
aquarium = lenght * width * height
litrage = aquarium / 1000
needed_litre = litrage * (1-0.17)
print(f'{needed_litre} lv.')