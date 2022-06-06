deposit = float(input())
term = int(input())
percent = float(input())
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
annual_interest = deposit * percent / 100
monthly = annual_interest / 12
total_sum = deposit + term * monthly
print(total_sum)