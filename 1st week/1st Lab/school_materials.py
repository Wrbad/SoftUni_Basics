pens = int(input())
markers = int(input())
detergent = int(input())
percent = int(input())
price_per_pen = 5.80
price_per_marker = 7.20
price_per_detergent = 1.20
sum = pens * price_per_pen + \
      markers * price_per_marker \
      + detergent * price_per_detergent
final_price = sum - sum * (percent / 100)
print(f'{final_price}''lv')