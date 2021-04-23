date = "13-04-2021T09:05AM"

p = date.split('T')
date = p[0]
split_date = date.split('-')
print(f"date = {split_date}")
print(f"Date = {split_date[0]}")
print(f"Month = {split_date[1]}")
print(f"Year = {split_date[2]}")