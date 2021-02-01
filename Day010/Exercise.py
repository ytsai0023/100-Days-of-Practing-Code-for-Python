def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
      else:
        print("Not leap year.")
    else:
      print("Leap year.")
  else:
    print("Not leap year.")

def days_in_month(year,month):
    """This is about
        doc strings 
    test."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    is_leap(year)
    if year % 4 == 0 and month == 2 :
        return 29
    else:
        return month_days[month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



