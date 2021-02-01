### string.format

```=python
name = "angEL".title()
print(name)

#Angel

```

### doc strings

```=python
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


```
