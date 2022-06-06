chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())
chicken_price = 10.35
fish_price = 12.40
vegan_price = 8.15
delivery = 2.50
menu_sum_price = chicken_menu * chicken_price +\
    fish_menu * fish_price +\
    vegan_menu * vegan_price
desert_price = menu_sum_price * 0.2
total_sum = menu_sum_price + desert_price + delivery
print(f'{total_sum}'' lv.')