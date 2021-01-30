import random

name_list = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

who_pay_bill = name_list[random.randint(0,len(name_list)-1)]

print(f"{who_pay_bill} is going to buy the meal today!")