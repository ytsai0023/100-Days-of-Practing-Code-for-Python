
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

amount = 0

if size  ==  'S':
  amount += 15
elif size == 'M':
  amount += 20
elif size == 'L':
  amount += 25

if add_pepperoni == 'Y' and size == 'S':
  amount += 2
elif add_pepperoni == 'Y':
  amount += 3

if extra_cheese == 'Y':
  amount += 1


print(f"Your final bill is: ${amount}.")






