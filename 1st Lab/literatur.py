book = int(input())
pages = int(input())
days = int(input())
full_time = book // pages
hours_per_day = full_time // days
print(hours_per_day)