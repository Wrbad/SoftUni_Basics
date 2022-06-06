nylon_for_meter2 = int(input())
paint_for_letter = int(input())
thinner = int(input())
hours = int(input())
nylon_price = 1.50
paint_price = 14.50
thinner_price = 5
bags_price = 0.40
materials_price = (nylon_for_meter2 + 2) * nylon_price + \
    paint_for_letter * 1.1 * paint_price  +\
    thinner * thinner_price\
    +bags_price
salary = materials_price * 0.3 * hours
total_sum = materials_price + salary
print(f'{total_sum}'' lv.')