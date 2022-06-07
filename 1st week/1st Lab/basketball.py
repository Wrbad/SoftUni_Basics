training_price = int(input())
sneakers_perecent = 0.4
dress_percent = 0.2
ball_percent = 0.25
accessoaries_percent = 0.2
sneakers_price = training_price - \
                 training_price * sneakers_perecent
dress_price = sneakers_price - \
              sneakers_price * dress_percent
ball_price = dress_price * ball_percent
accessoaries_price = ball_price * accessoaries_percent
total_sum = training_price + sneakers_price + dress_price + \
    ball_price + accessoaries_price
print(f'{total_sum} lv.')